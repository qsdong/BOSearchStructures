#!/home/share/miniconda3/envs/dqsGpyOpt/bin/python3
# -*- coding: utf-8 -*-

# worker runs SCFT program


import json
from collections import OrderedDict

import sys
import os
import socket
import subprocess as sp
import shutil
import time
import math
import argparse

import numpy as np


lib_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(lib_path)

from genjson import BlockCopolymer

from socket_msg import send_msg, recv_msg

from read_fet import SCFTRESULT

from phi_generator import PhiGenerator



def my_parse_args():
    parser = argparse.ArgumentParser(description='QingshuDong worker.py')
    parser.add_argument('--ip', type=str, default=None, help='ip address')
    parser.add_argument('--port', type=int, default=None, help='port')
    parser.add_argument('--spacegroup', type=int, default=230, metavar='spaceGroupNo', help='space group number')
    parser.add_argument('--cellratio', type=float, default=1.0, help='Lz = cellratio * Lx, cubic space groups will ignore this parameter')
    parser.add_argument('--basis', type=int, default=2, metavar='basisNum', help='basis vector number')
    parser.add_argument('--start_basis', type=int, default=0, metavar='startBasis', help=' start basis number')
    parser.add_argument('--bcp', type=str, default="AB", choices=['AB', 'ABC'], metavar='bcpType', help='bcpType: AB or ABC')
    parser.add_argument('--program', type=str, default="/home/share/scft2024", help='scft program path')
    parser.add_argument('--calPlane', type=str, default="zy", help='calculate plane for 2d space groups')
    args = parser.parse_args()
    return args


class ServerInfo():
    def __init__(self, IP = '', port = 0):
        self.IP = IP
        self.port = port

# request a job from optimizer server
def get_job(serverInfo,workerID):
    requestInfo = {'method':'get','workerID':workerID}    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((serverInfo.IP, serverInfo.port))
    send_msg(client, (json.dumps(requestInfo)).encode())
    from_server = recv_msg(client)                      
    json_server = json.loads(from_server)               
    client.close()
    # print(from_server.decode())
    return json_server

#  register worker to optimizer server
def regist_worker(serverInfo):
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname) # ip address of this machine
    pid = os.getpid() # pid of this process
    requestInfo = {'method':'regist','clientIP':ipaddr,'clientHostname':hostname,'pid':pid}
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((serverInfo.IP, serverInfo.port))
    send_msg(client, (json.dumps(requestInfo)).encode())
    from_server = recv_msg(client)
    json_server = json.loads(from_server)
    client.close()
    # print(from_server.decode())
    return json_server['workerID']

# report the result to optimizer server
def finish_report(serverInfo,finishInfo,workerID):
    hostname = socket.gethostname()
    ipaddr = socket.gethostbyname(hostname)
    pid = os.getpid()

    requestInfo = {'method':'finishReport','workerID':workerID,'clientIP':ipaddr,'clientHostname':hostname,'pid':pid}
    finishInfo.update(requestInfo)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((serverInfo.IP, serverInfo.port))
    send_msg(client, (json.dumps(finishInfo)).encode())
    from_server = recv_msg(client) 
    # json_server = json.loads(from_server)
    client.close()


def run_scft(para_dict, bcp, args, runtimes):
    scftProgram = f'{args.program} >aa.txt 2>&1' # note: no & at the end, otherwise the waiting will be invalid

    rootDir = para_dict['rootDir']

    phinName = "phin.txt"
    inputName = "input.json"

    os.chdir(rootDir) 

    if not os.path.isdir('No{}basis{}'.format(args.spacegroup, args.basis)):
        os.mkdir('No{}basis{}'.format(args.spacegroup, args.basis))
    os.chdir('No{}basis{}'.format(args.spacegroup, args.basis))

    if runtimes==1: 
        if not os.path.isdir(para_dict['paraDir']): # paraDir is iter001, iter002, ...
            os.mkdir(para_dict['paraDir']) 
        else:
            print(para_dict['paraDir'])
            print('folder exists',flush=True)
            return "errorFolderExists", np.nan

    os.chdir(para_dict['paraDir']) 

    # copy input.json to current folder
    shutil.copyfile(rootDir+inputName, inputName)


    with open(inputName, "r") as f:
        input_dict = json.load(f, object_pairs_hook=OrderedDict)

    output_dict = bcp.changePara(para_dict,input_dict)

    output_dict["Initializer"]["FileInitializer"]["Path"] = phinName
    output_dict['Initializer']["LevelsetInitializer"]["SpaceGroup"] = args.spacegroup

    with open("input.json", "w") as f:
        json.dump(output_dict, f, indent=4, separators=(',', ': '))

    # generate phin.txt
    phiGenerator = PhiGenerator(args.spacegroup, args.cellratio, input_dict, args.basis, args.start_basis, args.bcp, args.calPlane) # args.bcp = "AB" or "ABC"
    hkl = phiGenerator.generate_phin()

    if runtimes==1:
        with open("runlog.log","w") as fp:
            fp.write("space group = {}\n".format(args.spacegroup))
            fp.write("cell ratio = {}\n".format(args.cellratio))
            fp.write("basis:\n")
            for chkl in hkl:
                fp.write("{}\n".format(chkl))

    # run SCFT program
    a = sp.Popen(scftProgram, shell=True, stdout=sp.PIPE)
    a.wait()

    print('run scft in dir {}'.format(os.getcwd()),flush=True)

    fetCode,freeE,Lxyz = check_fet()
    ai = [np.nan for i in range(len(hkl))]

    delFiles = ["iterRecord.dat","phout.txt","printout.txt"]

    if fetCode=="Converged": 
        with open("runlog.log","a") as fp:
            fp.write("run {} times, converged\n".format(runtimes))
        return "correctFinished", freeE, ai, Lxyz
    else: 
        for i in delFiles:
            if os.path.isfile(i):
                os.remove(i)
        
        with open("runlog.log","a") as fp:
            fp.write("run {} times, error\n".format(runtimes))
        return fetCode, np.nan, ai, Lxyz  
    pass


def check_fet():
    fetCode = ""
    freeE = np.nan
    Lxyz = [np.nan,np.nan,np.nan]
    cRes = SCFTRESULT('fet.dat')

    if cRes.allInfo['isfile']:
        Lxyz = [cRes.allInfo['result_lx'],cRes.allInfo['result_ly'],cRes.allInfo['result_lz']]
        if math.isnan(sum(Lxyz)):
            fetCode = 'NaN'
        elif max(Lxyz)>20:
            fetCode = 'LargeLxyz'
        elif cRes.allInfo['result_inCompMax'] >1e-4 or cRes.allInfo['result_stressX'] >1e-4 or cRes.allInfo['result_stressY'] >1e-4 or cRes.allInfo['result_stressZ'] >1e-4 :
            fetCode = 'NotConverged'
        else:
            fetCode = 'Converged'
            freeE = cRes.allInfo['result_freeEnergy']
    else:
        print("file {}/{} not exists".format(os.getcwd(),cRes.filename),flush=True)
        fetCode = 'FileNotFound'
    
    return fetCode, freeE, Lxyz

def load_ph_bin(filename): # read ph.bin
    Nxyz = np.fromfile(filename, dtype=np.intc, count=3, offset=0) # intc is identical to C int (normally int32 or int64)
    # print(Nxyz[0].itemsize) # the size of intc is 4
    Lxyz = np.fromfile(filename, dtype=np.float64, count=3, offset=3*4)
    # print(Lxyz[0].itemsize) # the size of float64 is 8
    ph = np.fromfile(filename, dtype=np.float64, count=-1, offset=3*(4+8)) # read all remaining data
    NxNyNz = Nxyz[0]*Nxyz[1]*Nxyz[2]
    # ph = ph.reshape([3,Nxyz[0],Nxyz[1],Nxyz[2]])
    try:
        ph = ph.reshape([-1,NxNyNz])
    except:
        raise ValueError("wrong file size")
    return ph, Nxyz, Lxyz



if __name__ == "__main__":

    args = my_parse_args()
    print(args)
    if not args.ip or not args.port:
        raise Exception("ip and port are both required")

    serverInfo = ServerInfo(IP = args.ip, port = args.port)
    workerID = regist_worker(serverInfo) # register the worker, get workerID

    if workerID >= 0: # successfully registered
        bcp = BlockCopolymer() # create a BlockCopolymer object

        while True: # stop when no new jobs
            para_dict = get_job(serverInfo, workerID) # get a new job
            if para_dict['waitTime'] > 0:
                time.sleep(para_dict['waitTime'])
            elif para_dict['waitTime'] < 0: # stop the worker
                break
            else: # normal job
                scftCode, freeE, ai, Lxyz  = run_scft(para_dict, bcp, args,  runtimes=1) # run SCFT program
                if scftCode == "errorFolderExists": # folder exists error
                    print("errorFolderExists:",para_dict)

                finishInfo = {"statusCode":scftCode,"iter":para_dict["iter"],"freeE":freeE, "ai":ai, "Lxyz":Lxyz}
                finish_report(serverInfo,finishInfo,workerID)
            pass

        finishInfo = {"statusCode":"noJobs","iter":0,"freeE":np.nan}
        finish_report(serverInfo,finishInfo,workerID)
    else:
        print("error worker ID",flush=True)
    print("no new jobs, worker exit",flush=True)

