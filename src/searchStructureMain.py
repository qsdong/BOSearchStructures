#!/home/share/miniconda3/envs/dqsGpyOpt/bin/python3
# -*- coding: utf-8 -*-

# main program
# this program will allocate resources for optimizer and workers
# this program will exit after allocating resources for workers

# consider replace srun and its parameters if you are not using slurm


import subprocess as sp
import socket
import json
import os
import sys
import utils
from socket_msg import send_msg, recv_msg


lib_path = os.path.abspath(os.path.dirname(__file__))  
sys.path.append(lib_path) 



def allocQueueJobWorker(myargs,optimizerIP,optimizerPort):
    lib_path = os.path.abspath(os.path.dirname(__file__)) 
    if not os.path.isdir("log"): 
        os.mkdir("log")
    for i in range(myargs['worker']):
        shellscript = f"srun --partition={myargs['partition']} --gpus=1 --cpus-per-gpu=1 {lib_path}/worker.py \
            --ip {optimizerIP} --port {optimizerPort} --spacegroup {myargs['spacegroup']} --cellratio {myargs['cellratio']} \
            --basis {myargs['basis']} --start_basis {myargs['start_basis']} --bcp {myargs['bcp']} --program {myargs['program']} \
            --calPlane {myargs['calPlane']} >./log/workerlog{i:0>2d}.txt 2>&1 &"
        a = sp.Popen(shellscript,shell=True,stdout=sp.PIPE)
    pass



def allocQueueJobOptimizer(cpupartition,mainServerInfo, optimizerThread):
    lib_path = os.path.abspath(os.path.dirname(__file__))
    if not os.path.isdir("log"):
        os.mkdir("log")
    shellscript = f"srun --partition={cpupartition} --cpus-per-task={optimizerThread} {lib_path}/optimizer.py \
                    --ip {mainServerInfo.ip} --port {mainServerInfo.port}  >./log/optimizerlog.txt 2>&1 &"
    
    a = sp.Popen(shellscript,shell=True,stdout=sp.PIPE)
    pass


# ************************************script begins***********************************

if __name__ == '__main__':

    print("version 11: 2023-04-24")

    # get ip and port of current machine
    mainServerInfo = utils.get_ip_port()
    print("mainServerInfo:", mainServerInfo.ip, mainServerInfo.port)

    # read para.json file
    myargs_main = utils.MY_ARGS("para.json")
    myargs_main.read_para_file_json()
    myargs_main.disp_para()

    # fflush
    sys.stdout.flush()

    # allocate resources for optimizer
    allocQueueJobOptimizer(myargs_main.cpupartition,mainServerInfo,myargs_main.optimizerThread) 

    # create a socket to accept optimizer's connection
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind((mainServerInfo.ip, mainServerInfo.port))
    serv.listen(8)
    print("main server is listening...")

    conn, addr = serv.accept()  # wait for optimizer to connect
    data = recv_msg(conn)       # accept message from optimizer
    from_client = data.decode() # decode message

    data_json = json.loads(from_client,strict=False) # convert message to json format
    print("data from optimizer:")
    # if not dict, print directly; if dict, print key and value recursively
    for key, value in data_json.items():
        if not isinstance(value,dict):
            print(key+":",value)
        else:
            for key2,value2 in value.items():
                print(key+":",key2+":",value2)

    if data_json["method"] =='optimizerReady': # optimizer is ready

        myargs = data_json["myargs"]               # optimizer's parameters
        optimizerIP = data_json["optimizerIP"]     # optimizer's ip address
        optimizerPort = data_json["optimizerPort"] # optimizer's port

        para_dict = {"nodata":0}

        send_msg(conn, (json.dumps(para_dict)).encode()) # send message to optimizer
        conn.close() # close connection
        serv.close() # close socket
        print("main server is closed")
    else:
        print("error: optimizer send wrong message!")
    
    # allocate resources for workers
    allocQueueJobWorker(myargs,optimizerIP,optimizerPort)
    print("worker is allocated")

    print("main server exits")
    

# ************************************script ends***********************************

# you can set an alias in ~/.bashrc, for example:
# alias runBO='/home/share/dqsGpyOpt/ver11/searchStructureMain.py > a.log 2>&1 &'