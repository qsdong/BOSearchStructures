#!/home/share/miniconda3/envs/dqsGpyOpt/bin/python3
# -*- coding: utf-8 -*-


# optimizer communicate with worker
# optimizer is a server, accept worker's request


import time
import socket
import json

import numpy as np
import os
import argparse
import sys

lib_path = os.path.abspath(os.path.dirname(__file__))  
sys.path.append(lib_path) 

from next_para_noWait import AllParaPoint_NoWait
from socket_msg import send_msg, recv_msg

import utils


def my_parse_args():
    parser = argparse.ArgumentParser(description='QingshuDong optimizer.py')
    parser.add_argument('--ip', type=str, default=None, help='main server ip address')
    parser.add_argument('--port', type=int, default=None, help='main server port')
    parser.add_argument('--file', type=str, default="para.json", help='parafilename')
    args = parser.parse_args()
    return args



def mainLoop():
    mainServerInfo = my_parse_args()
    print("args form main server:", mainServerInfo)

    # get ip and port of current machine
    optimizerInfo = utils.get_ip_port()
    print("optimizerInfo:", optimizerInfo.ip, optimizerInfo.port)

    # read para.json file
    myargs = utils.MY_ARGS(mainServerInfo.file)
    myargs.read_para_file_json()
    myargs.disp_para()
    myargs.check_para_input()

    # create workerList
    workerList = []
    for i in range(myargs.worker):
        worker = utils.WorkerInfo(i)
        workerList.append(worker)   
    
    
    levelCount, lxyzCount, thetaCount, squenceCount  = myargs.cal_variable_count() # calculate the number of variables
    print(f"levelCount: {levelCount}, lxyzCount: {lxyzCount}, thetaCount: {thetaCount}, squenceCount: {squenceCount}")

    


    # read step_record.txt file, if exists, read history record from file and continue to run
    step_record_filename = 'step_record.txt'
    if os.path.isfile(step_record_filename):
        print("load step_record.txt")
        a = np.loadtxt(step_record_filename, dtype=float, comments='#', delimiter=' ')
        x_step = a[:,:-1]
        y_step = a[:,-1].reshape(-1,1) # the last column is the free energy
    else:
        print("no step_record.txt, start from nan")
        x_step = np.ones((1,myargs.basis+thetaCount+levelCount+lxyzCount+squenceCount))*np.nan
        y_step = np.array([[np.nan]])
    
    if len(y_step)>= myargs.step:
        print('nothing to do')
        exit(1)

    if len(x_step[0]) != myargs.basis + thetaCount + levelCount + lxyzCount + squenceCount:
        raise ValueError('basis number not match')

    rootDir = os.getcwd()+'/' # get current working directory

    os.chdir(rootDir)

    # create a AllParaPoint_NoWait object
    APP = AllParaPoint_NoWait(args=myargs, x_step_init=x_step, y_step_init=y_step, rootDir=rootDir,
                              thetaCount=thetaCount, levelCount=levelCount, lxyzCount=lxyzCount, squenceCount=squenceCount) 


    # create a socket, notify the main server that the optimizer has been started
    requestInfo = {'method':'optimizerReady','myargs':myargs.to_dict(),'optimizerIP':optimizerInfo.ip,'optimizerPort':optimizerInfo.port}
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((mainServerInfo.ip, mainServerInfo.port))
    send_msg(client, (json.dumps(requestInfo)).encode())
    from_server = recv_msg(client)                      
    # json_server = json.loads(from_server)             
    client.close()


    # create a socket, used to accept worker's connection
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind((optimizerInfo.ip, optimizerInfo.port)) # bind ip and port
    serv.listen(128)

    print("optimizer is listening...")
    noJobCount = 0 # record how many workers have finished their jobs


    while True: # main loop
        conn, addr = serv.accept()  # wait for worker's connection
        data = recv_msg(conn)       # receive message from worker
        from_client = data.decode() # decode message

        data_json = json.loads(from_client,strict=False) # convert message to json format
        data_json["ipaddr"] = addr[0] # add worker's ip address to json

        localtime = time.strftime("%Y%m%d-%H:%M:%S",time.localtime())

        if data_json["method"] =='get': # worker ask for next task 
            para_dict = APP.get_next_para() # get next task parameters
            send_msg(conn, (json.dumps(para_dict)).encode())   # send parameters to worker
            workerList[data_json["workerID"]].status = 'running' # update worker status to "running"

            utils.writeLog("{}: iter {}, get from {} workerID = {}, wait {} s".format(localtime, APP.bo_model.iter_count, \
                    addr[0], data_json['workerID'], para_dict['waitTime'] )) # record log

        elif data_json["method"] =='regist': # worker send a registration request
            para_dict = {'workerID':-1}
            for i in range(len(workerList)):
                if len(workerList[i].workerIP)==0: 
                    para_dict['workerID'] = workerList[i].workerID
                    workerList[i].workerIP = addr[0]
                    break
            send_msg(conn, (json.dumps(para_dict)).encode()) # send workerID to worker

            utils.writeLog("{}: regist from {}, assign workerID = {}".format(localtime, addr[0], para_dict['workerID']))
            pass

        elif data_json["method"] =='finishReport': # worker finish a task
            workerList[data_json["workerID"]].status = data_json["statusCode"]
            if data_json["statusCode"] in ['reRun','correctFinished','errorFinished']:
                workerList[data_json["workerID"]].finishedJobCount += 1
            if data_json["statusCode"] in ['NotConverged','LargeLxyz']:
                workerList[data_json["workerID"]].finishedJobCountNotConverged += 1

            if data_json["statusCode"] not in ["reRun","noJobs","FileNotFound","errorFolderExists"]: # update result
                APP.update_scft_result(data_json["iter"], data_json["freeE"], data_json["ai"], data_json["Lxyz"],data_json["statusCode"])

                APP.dump_result(step_record_filename) # save history record to file

            para_dict = {"nodata":0} # no data to send

            send_msg(conn, (json.dumps(para_dict)).encode()) # send message to worker

            log = "{}: {} workerID = {} finished a job with code {}".format(localtime, addr[0], data_json['workerID'],data_json["statusCode"])

            utils.writeLog(log)

        else:
            conn.close()
            raise ValueError('method not supported: {}'.format(data_json["method"]))

        conn.close() # close connection
        


        if data_json["method"] =='finishReport':  
            if data_json["statusCode"] == "noJobs":  # if no new jobs, noJobCount +1
                noJobCount +=1
        if noJobCount == myargs.worker:       # all workers have finished their jobs
            for i in range(len(workerList)):
                print('worker{:0>2d} run SCFT {} + {} times'.format(i,workerList[i].finishedJobCount,workerList[i].finishedJobCountNotConverged))
            break # exit main loop
    
    APP.dump_result(step_record_filename) # save history record to file
    serv.close() # close socket
    print("optimizer server is closed")
    pass





if __name__ == "__main__":
    print("version 11: 2023-04-10")

    time0 = time.time() 
    mainLoop()
    time1 = time.time()
    print("optimizer total running time {} s".format(time1-time0))
    







