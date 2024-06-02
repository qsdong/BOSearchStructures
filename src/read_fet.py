#!/usr/bin/python3
# dongqs at 2022.07.26

import os
import math


# read SCFT result from fet.dat

class SCFTRESULT:
    def __init__(self,filename = ''):
        self.filename = filename
        self.allInfo = {'isfile':False}
        self.fileContents = []
        if os.path.isfile(filename):
            self.allInfo['isfile'] = True
            self.readFet(filename)
            self.getInfo()
        pass
    def getInfo(self):
        for i in self.fileContents:
            if 'para' in i or 'result' in i:
                _, iPara, iData = i.split()
                self.allInfo["result_"+iPara] = float(iData)
        pass

    def readFet(self,fullFileName):
        if os.path.isfile(fullFileName):
            with  open(fullFileName,"r") as fp:
                self.fileContents = fp.readlines()
                fp.close()




#################################################################

if __name__ == "__main__":
    
    cRes = SCFTRESULT('fet.dat')

    if cRes.allInfo['isfile']:
        Lxyz = [cRes.allInfo['result_lx'],cRes.allInfo['result_ly'],cRes.allInfo['result_lz']]
        if math.isnan(sum(Lxyz)):
            statusCode = 'NaN'
        elif max(Lxyz)>50:
            statusCode = 'LargeLxyz'
        elif cRes.allInfo['result_inCompMax'] >1e-4 or cRes.allInfo['result_stressX'] >2e-4 or cRes.allInfo['result_stressY'] >2e-4 or cRes.allInfo['result_stressZ'] >2e-4 :
            statusCode = 'NotConverged'
        else:
            statusCode = 'Converged'
    else:
        print("file {}/{} not exists".format(os.getcwd(),cRes.filename))
        statusCode = 'FileNotFound'
    
    print(statusCode)



# A sample of fet.dat

'''
para: xABN 20.000000
para: xBAN 20.000000
result: stressX 7.26337809e-10
result: stressY 7.26072421e-10
result: stressZ 7.26261808e-10
result: lx 9.438569
result: ly 9.438569
result: lz 9.438569
result: lx_full 9.4385691649334760
result: ly_full 9.4385691651625621
result: lz_full 9.4385691653054256
result: freeEnergy 3.9182330420650322
result: freeAB_sum 2.0614200967349392
result: freeAB 2.0614200967349392
result: freeBA 2.0614200967349392
result: freeW -4.1228401927451328
result: freeS 5.9796531380752258
result: freeDiff 3.35838024e-11
result: inCompMax 8.57695515e-09
result: Q0 0.0025297035979276
result: VolumeFraction0 1.000000
result: sumVolume 1.000000
result: activity0 395.303229
'''