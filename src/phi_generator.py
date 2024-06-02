#!/home/dongqs/sdd/venv_gcn/bin/python3
# -*- coding: utf-8 -*-

# generate phin.txt file

import numpy as np
from scipy.interpolate import interpn

import sys
import os
lib_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(lib_path)

import calF


class StructureFactor(object):
    def __init__(self, spaceGroupNo, jsonDict, basisNumber):
        self.spaceGroupNo = spaceGroupNo
        self.jsonDict = jsonDict
        self.basisNumber = basisNumber

        if 143 <= self.spaceGroupNo <= 194: # trigonal/hexagonal space groups
            self.Nx, self.Ny, self.Nz = 64, 64, 64 # using 646464 to calculate F, then interpolate phi according to NxNyNz in input.json

        elif 313 <= self.spaceGroupNo <= 317: # 2d space groups
            self.Nx, self.Ny, self.Nz = 64, 64, 1 # using 6464 to calculate F, then interpolate phi according to NxNyNz in input.json
        else:
            self.Nx, self.Ny, self.Nz = self.jsonDict['Solver']['PseudospectralMethod']["SpaceGridSize"][0:3]
            if self.Nx == 1:
                self.Nx, self.Nz = self.Nz, self.Nx
        # note that the Nx,Nx,Nz are only used to calculate F, the actual Nx,Ny,Nz are in input.json

        self.ai = self.jsonDict['Initializer']["LevelsetInitializer"]["Ai"] # f_{hkl} in the paper
        
        self.theta = self.jsonDict['Initializer']["LevelsetInitializer"]["theta"]


class PhiGenerator():
    def __init__(self, spaceGroupNo, cellratio, jsonDict, basisNumber,startBasis, bcpType, calPlane):
        self.spaceGroupNo = spaceGroupNo
        self.cellratio = cellratio
        self.jsonDict = jsonDict
        self.basisNumber = basisNumber
        self.startBasis = startBasis
        self.bcpType = bcpType
        self.calPlane = calPlane

        self.Nx, self.Ny, self.Nz = self.jsonDict['Solver']['PseudospectralMethod']["SpaceGridSize"][0:3]
        self.Lx, self.Ly, self.Lz = self.jsonDict['Initializer']['UnitCell']["Length"][0:3]
        self.ai = self.jsonDict['Initializer']["LevelsetInitializer"]["Ai"]        # list
        self.theta = self.jsonDict['Initializer']["LevelsetInitializer"]["theta"]  # list
        self.level = self.jsonDict['Initializer']["LevelsetInitializer"]["Level"]  # list
        self.sequence = int(self.jsonDict['Initializer']["LevelsetInitializer"]["Sequence"])  # int
        self.NxNyNz = self.Nx*self.Ny*self.Nz

        self.SF = StructureFactor(self.spaceGroupNo, self.jsonDict, self.basisNumber)
    
    def __interpHex(self, F):
        [xtmp,ytmp,zq] = np.meshgrid(np.linspace(0,1-1.0/self.Nx,self.Nx),np.linspace(0,np.sqrt(3.0)-np.sqrt(3.0)/self.Ny,self.Ny),np.linspace(0,1-1.0/self.Nz,self.Nz),indexing='ij')

        xq = xtmp-np.cos(np.pi/3)/np.sin(np.pi/3)*ytmp
        yq = xtmp+(1-np.cos(np.pi/3))/np.sin(np.pi/3)*ytmp

        xq[xq<0] = xq[xq<0]+1
        yq[yq<0] = yq[yq<0]+1
        xq[xq>1] = xq[xq>1]-1
        yq[yq>1] = yq[yq>1]-1

        xdata = np.linspace(0,1-1.0/64,64) 
        ydata = np.linspace(0,1-1.0/64,64)
        zdata = np.linspace(0,1-1.0/64,64)

        F = interpn((xdata,ydata,zdata),F,(xq,yq,zq),method='linear',bounds_error=False,fill_value=None)
        '''fill_value : number, optional
        If provided, the value to use for points outside of the
        interpolation domain. If None, values outside
        the domain are extrapolated.  Extrapolation is not supported by method
        "splinef2d".'''
        return F
    
    def __interpHex_2d(self, F):
        if self.Nz == 1:  # not recommended to set Nz=1 in input.json
            Nx = self.Nx
        elif self.Nx == 1: # recommended
            Nx = self.Nz

        [xtmp,ytmp] = np.meshgrid(np.linspace(0,1-1.0/Nx,Nx),np.linspace(0,np.sqrt(3.0)-np.sqrt(3.0)/self.Ny,self.Ny),indexing='ij')

        xq = xtmp-np.cos(np.pi/3)/np.sin(np.pi/3)*ytmp
        yq = xtmp+(1-np.cos(np.pi/3))/np.sin(np.pi/3)*ytmp

        xq[xq<0] = xq[xq<0]+1
        yq[yq<0] = yq[yq<0]+1
        xq[xq>1] = xq[xq>1]-1
        yq[yq>1] = yq[yq>1]-1

        xdata = np.linspace(0,1-1.0/64,64) 
        ydata = np.linspace(0,1-1.0/64,64)

        F = interpn((xdata,ydata),F,(xq,yq),method='linear',bounds_error=False,fill_value=None)
        '''fill_value : number, optional
        If provided, the value to use for points outside of the
        interpolation domain. If None, values outside
        the domain are extrapolated.  Extrapolation is not supported by method
        "splinef2d".'''
        
        return F
        pass


    def __save_phin_AB(self, F):
        # AB， level0 [0,1]
        maxValue = np.max(F) # Maximum of the flattened array
        minValue = np.min(F) # Minimum of the flattened array
        F = (F-minValue)/(maxValue-minValue) # normalize to [0,1]

        if 143<= self.spaceGroupNo <= 194: # trigonal/hexagonal space groups
            F = self.__interpHex(F)
        elif 313 <= self.spaceGroupNo <= 317:
            F = self.__interpHex_2d(F)
        elif 300 <= self.spaceGroupNo <= 312:
            pass

        if 300 <= self.spaceGroupNo <= 317:
            if self.calPlane == 'zy':
                F = F.T

        F = F.flatten()
        ph = np.zeros((self.NxNyNz,4))

        if len(self.level) == 0:
            print("level empty, use F directly")
            ph[:,0] = F                 # phi_{A}
            ph[:,1] = 1-ph[:,0]         # phi_{B}
            np.savetxt('phin.txt',ph,fmt='%f %f %d %d',
                    header='{} {} {}\n{} {} {}'.format(self.Nx,self.Ny,self.Nz,self.Lx,self.Ly,self.Lz),comments='') # float format
        else:
            ph[F>self.level[0],0] = 1.0 # phi_{A}
            ph[:,1] = 1-ph[:,0]         # phi_{B}
            np.savetxt('phin.txt',ph,fmt='%d %d %d %d',
                    header='{} {} {}\n{} {} {}'.format(self.Nx,self.Ny,self.Nz,self.Lx,self.Ly,self.Lz),comments='') # int format
        pass


    def __save_phin_ABC(self, F):
        # ABC, level0 [0,1], level1 [-1,0]
        maxValue = np.max(F) # Maximum of the flattened array
        minValue = np.min(F) # Minimum of the flattened array
        F = ((F-minValue)/(maxValue-minValue))*2-1.0 # normalize to [-1,1]
        
        if 143<= self.spaceGroupNo <= 194.99: # trigonal/hexagonal space groups
            F = self.__interpHex(F)
        elif 313 <= self.spaceGroupNo <= 317:
            F = self.__interpHex_2d(F)
        
        if 300 <= self.spaceGroupNo <= 317:
            if self.calPlane == 'zy':
                F = F.T
        
        F = F.flatten()
        ph = np.zeros((self.NxNyNz,6))
        if self.sequence == 0:
            idx0,idx1,idx2 = 0,1,2
        elif self.sequence == 1:
            idx0,idx1,idx2 = 0,2,1
        elif self.sequence == 2:
            idx0,idx1,idx2 = 1,0,2
        else:
            raise ValueError('sequence not supported')
        if len(self.level) == 0:
            print("level empty, use 0.5 and -0.5 as default")
            ph[F>0.5,idx0] = 1.0    # phi_{A}
            ph[F<-0.5,idx2] = 1.0   # phi_{C}
        else:
            ph[F>self.level[0],idx0] = 1.0   # phi_{A}
            ph[F<self.level[1],idx2] = 1.0   # phi_{C}
        ph[:,idx1] = 1-ph[:,idx0]-ph[:,idx2] # phi_{B}
        np.savetxt('phin.txt',ph,fmt='%d %d %d %d %d %d',header='{} {} {}\n{} {} {}'.format(self.Nx,self.Ny,self.Nz,self.Lx,self.Ly,self.Lz),comments='')
        pass



    def generate_phin(self):
        F = None
        numTheta = None

        strSpaceGroupNo = str(self.spaceGroupNo)
        funcName = 'calF_' + strSpaceGroupNo
        if np.abs(self.cellratio - 0.5)<1e-6:
            funcName += '_0d5'
        elif np.abs(self.cellratio - 2.0)<1e-6:
            funcName += '_2d0'

        if not hasattr(calF, funcName):
            raise ValueError('{} not supported'.format(funcName))
        
        func = getattr(calF, funcName)
        F, numTheta, hkl = func(self.SF, startBasis=self.startBasis)

        
        if numTheta != len(self.theta):
            print("numTheta = {}, len(self.theta) = {}".format(numTheta, len(self.theta)))
            raise ValueError('numTheta != len(self.theta)')
        
        if self.bcpType == 'AB':
            self.__save_phin_AB(F)
        elif self.bcpType == 'ABC':
            self.__save_phin_ABC(F)
        else:
            raise ValueError('bcpType not supported')
        
        return hkl
