import json
from collections import OrderedDict
import socket
import subprocess as sp
import fcntl
import os


from get_thetaCount import get_thetaCount
from get_thetaCount_0d5 import get_thetaCount_0d5
from get_thetaCount_2d0 import get_thetaCount_2d0


class ServerInfo(): 
    def __init__(self, ip = '', port = 0):
        self.ip = ip
        self.port = port

class WorkerInfo(): 
    def __init__(self,ID):
        self.workerID = ID                   
        self.workerIP = ''                   
        self.status = 'waiting'              
        self.finishedJobCount = 0            
        self.finishedJobCountNotConverged = 0

class MY_ARGS():
    def __init__(self, parafilename = "para.json", port = 0):
        self.step = 11              # maxRunIter
        self.port = port            # port
        self.worker = 4             # workerNumber
        self.spacegroup = 230       # spaceGroupNo
        self.basis = 2              # basisNum
        self.start_basis = 0        # startBasis
        self.bcp = "AB"             # bcpType
        self.weight = 1             # acquisition_weight
        self.fixlevel = False       # fix level value at 0.5 (and -0.5 for ABC)
        self.cellratio = 1.0        # Lz = cellratio * Lx, cubic space groups will ignore this parameter
        self.fixratio = False       # fix initial ratio of Lz/Lx, cubic space groups will ignore this parameter
        self.lxyzBounds = [2, 20]   # lxyzBounds [min, max] Rg
        self.calPlane = "zy"        # calculate plane for 2d space groups, "zy" is recommended
        self.rand = False           # randomly generate structure parameters
        self.distance_weight = 0.0  # distance weight
        self.distance_sigma = 0.01  # distance sigma
        self.distance_lambda = 0.01 # distance lambda
        self.list_size = 1000       # list size to calcute distance , similar to tabu length
        self.file = parafilename    # parameter file name
        self.partition = "amd_4090,intel_4090,amd_3090,intel_2080ti,intel_2080"
        self.cpupartition = "intel_Xeon,amd_4090,amd_3090"
        self.program = "/home/share/scft2024" # scft program path
        self.optimizerThread = 4    # optimizer thread number

    def read_para_file_json(self):
        with open(self.file, 'r') as file:
            data = json.load(file)
        for key, value in data.items():
            if key in self.__dict__:
                if value == 'True' or value == 'true':
                    value = True
                elif value == 'False' or value == 'false':
                    value = False
                self.__dict__[key] = value
            else:
                print(f"Warning: {key} is not a valid parameter name.")
        for key, value in self.__dict__.items():
            if key not in data and key != 'port':
                print(f"Warning: {key} is using default value: {value}")
    
    def disp_para(self):
        for key, value in self.__dict__.items():
            if key == 'port':
                continue
            print(f"{key}: {value}")
        print("-------------------")
    def to_dict(self):
        return self.__dict__
    
    def cal_variable_count(self):
        if self.bcp == 'AB':   # AB type block copolymer
            squenceCount = 0
        elif self.bcp == 'ABC': # ABC type block copolymer
            squenceCount = 1
        else:
            raise ValueError('bcp type not supported')

        if self.fixlevel:
            levelCount = 0
        else:
            if self.bcp == 'AB':
                levelCount = 1
            elif self.bcp == 'ABC':
                levelCount = 2
            else:
                raise ValueError('bcp type not supported')

        if 195 <= self.spacegroup <= 230: # Cubic space groups
            lxyzCount = 1 #  lx
        elif 143 <= self.spacegroup <= 194: # Triagonal and Hexagonal space groups
            if self.fixratio:
                lxyzCount = 1
            else:
                lxyzCount= 2 # lx, lz (ly = sqrt(3)*lx)
        elif 75 <= self.spacegroup <= 142: # Tetragonal space groups
            if self.fixratio: 
                lxyzCount = 1
            else:
                lxyzCount = 2 # lx, lz (ly = lx)
        elif 16 <= self.spacegroup <= 74: # Orthorhombic space groups
            lxyzCount = 3 # lx, ly, lz
        elif 310 <= self.spacegroup <= 317: # 2d planner groups
            lxyzCount = 1 # lx
        else:
            raise ValueError('spaceGroupNo not supported')
        

        # calculate thetaCount
        if abs(self.cellratio-0.5)<1e-6:
            thetaCount = get_thetaCount_0d5(self.spacegroup, self.basis, self.start_basis)
        elif abs(self.cellratio-2.0)<1e-6:
            thetaCount = get_thetaCount_2d0(self.spacegroup, self.basis, self.start_basis)
        else:
            thetaCount = get_thetaCount(self.spacegroup, self.basis, self.start_basis)
        return levelCount, lxyzCount, thetaCount, squenceCount
    
    def check_para_input(self):
        # ensure basis+start_basis <= 32
        if 195 <= self.spacegroup <= 230:
            if self.basis + self.start_basis > 32:
                raise ValueError('basis number not supported for cubic space groups: {}'.format(self.basis))
        elif 143 <= self.spacegroup <= 194:
            if self.basis + self.start_basis > 32:
                raise ValueError('basis number not supported for trigonal/hexagonal space groups: {}'.format(self.basis))
        elif 75 <= self.spacegroup <= 142:
            if self.basis + self.start_basis > 32:
                raise ValueError('basis number not supported for tetragonal space groups: {}'.format(self.basis))
        elif 310 <= self.spacegroup <= 317:
            if self.basis + self.start_basis > 32:
                raise ValueError('basis number not supported for 2d planner groups: {}'.format(self.basis))
        else:
            raise ValueError('spaceGroupNo not supported: {}'.format(self.spacegroup))
        
        
        with open("input.json", "r") as f:
            input_dict = json.load(f, object_pairs_hook=OrderedDict)
        
        changeFlag = False
        if "LevelsetInitializer" not in input_dict["Initializer"]:
            levelsetInitializer = OrderedDict({"SpaceGroup":0,"Level":[],"theta":[],"Ai":[]})
            input_dict["Initializer"]["LevelsetInitializer"] = levelsetInitializer
            changeFlag = True
        if "AndersonMixingType" not in input_dict["Iteration"]["AndersonMixing"]:
            input_dict["Iteration"]["AndersonMixing"]["AndersonMixingType"] = "OLD"
            changeFlag = True
        Nx, Ny, Nz = input_dict['Solver']['PseudospectralMethod']["SpaceGridSize"][0:3]
        if self.calPlane == "zy" and Nz == 1:
            input_dict['Solver']['PseudospectralMethod']["SpaceGridSize"][0:3] = [Nz, Ny, Nx]
            changeFlag = True
        if self.calPlane == "xy" and Nx == 1:
            input_dict['Solver']['PseudospectralMethod']["SpaceGridSize"][0:3] = [Nz, Ny, Nx]
            changeFlag = True
        if "Sequence" not in input_dict["Initializer"]["LevelsetInitializer"]:
            input_dict["Initializer"]["LevelsetInitializer"]["Sequence"] = 0
            changeFlag = True

        # cheange the parameters in the json file
        if changeFlag:
            with open("input.json", "w") as f:
                json.dump(input_dict, f, indent=4, separators=(',', ': '))
    pass


def get_ip_port():
    username = os.path.expanduser("~").split('/')[-1]
    lockfile = open("/tmp/"+username+"_port.lock", "w")
    fcntl.flock(lockfile, fcntl.LOCK_EX)

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    # ss -tuln | awk '{print $5}'
    a = sp.Popen("ss -tuln | awk '{print $5}' ", shell=True,stdout=sp.PIPE)
    b = a.stdout.read().decode('utf-8').split('\n')
    c = [i.split(':')[-1] for i in b if ':' in i]
    d = [i for i in c if i != '']
    e = [int(i) for i in d if i != '']
    f = list(set(e))
    f.sort() 
    # print(f)
    for i in range(10000, 65535):
        if i not in f:
            port = i
            break
    
    fcntl.flock(lockfile, fcntl.LOCK_UN)
    lockfile.close()

    return ServerInfo(ip, port)

def writeLog(msg):
    with open('log/messageRecord.txt','a') as fp:
        fp.write(msg+'\n')
        fp.close()


if __name__ == "__main__":
    myargs = MY_ARGS()
    # myargs.disp_para()
    print("-------------------")
    myargs.read_para_file_json()
    print("-------------------")
    # myargs.disp_para()
