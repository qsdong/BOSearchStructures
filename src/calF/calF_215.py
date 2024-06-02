# Generated at 2023-12-16 14:03:04
# Qingshu Dong

import numpy as np

def  calF_215(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([6, 12, 8, 6, 24, 24, 12, 24, 6, 24, 24, 8, 24, 48, 6, 24, 24, 12, 24, 24, 24, 48, 24, 24, 24, 6, 48, 24, 8, 24, 48, 24])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 215.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA100 = 8*cos(2*x*pi) + 8*cos(2*y*pi) + 8*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA100*Multi[idx_a]
        hkl.append([1,0,0])
        idx_a += 1

    if 1 in usedBasis:
        fA110 = 8*cos(2*x*pi)*cos(2*y*pi) + 8*cos(2*x*pi)*cos(2*z*pi) + 8*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 2 in usedBasis:
        fA111 = 24*cos(2*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA111*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB111 = -24*sin(2*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB111*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,1])
        idx_a += 1

    if 3 in usedBasis:
        fA200 = 8*cos(4*x*pi) + 8*cos(4*y*pi) + 8*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 4 in usedBasis:
        fA210 = 4*cos(2*x*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*(2*cos(2*x*pi)**2 - 1) + 4*cos(2*x*pi)*(2*cos(2*z*pi)**2 - 1) + 4*cos(2*z*pi)*(2*cos(2*x*pi)**2 - 1) + 4*cos(2*y*pi)*(2*cos(2*z*pi)**2 - 1) + 4*cos(2*z*pi)*(2*cos(2*y*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA210*Multi[idx_a]
        hkl.append([2,1,0])
        idx_a += 1

    if 5 in usedBasis:
        fA211 = 8*cos(2*x*pi)*cos(2*y*pi)*(2*cos(2*z*pi)**2 - 1) + 8*cos(2*x*pi)*cos(2*z*pi)*(2*cos(2*y*pi)**2 - 1) + 8*cos(2*y*pi)*cos(2*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = - 8*sin(2*x*pi)*sin(2*y*pi)*sin(4*z*pi) - 8*sin(2*x*pi)*sin(4*y*pi)*sin(2*z*pi) - 8*sin(4*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 6 in usedBasis:
        fA220 = 8*cos(4*x*pi)*cos(4*y*pi) + 8*cos(4*x*pi)*cos(4*z*pi) + 8*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 7 in usedBasis:
        fA221 = 8*cos(2*x*pi)*(2*cos(2*y*pi)**2 - 1)*(2*cos(2*z*pi)**2 - 1) + 8*cos(2*y*pi)*(2*cos(2*x*pi)**2 - 1)*(2*cos(2*z*pi)**2 - 1) + 8*cos(2*z*pi)*(2*cos(2*x*pi)**2 - 1)*(2*cos(2*y*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA221*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB221 = - 8*sin(2*x*pi)*sin(4*y*pi)*sin(4*z*pi) - 8*sin(4*x*pi)*sin(2*y*pi)*sin(4*z*pi) - 8*sin(4*x*pi)*sin(4*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB221*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,1])
        idx_a += 1

    if 8 in usedBasis:
        fA300 = 8*cos(6*x*pi) + 8*cos(6*y*pi) + 8*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA300*Multi[idx_a]
        hkl.append([3,0,0])
        idx_a += 1

    if 9 in usedBasis:
        fA310 = 4*cos(2*x*pi)*cos(6*y*pi) + 4*cos(6*x*pi)*cos(2*y*pi) + 4*cos(2*x*pi)*cos(6*z*pi) + 4*cos(6*x*pi)*cos(2*z*pi) + 4*cos(2*y*pi)*cos(6*z*pi) + 4*cos(6*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA310*Multi[idx_a]
        hkl.append([3,1,0])
        idx_a += 1

    if 10 in usedBasis:
        fA311 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 8*cos(2*x*pi)*cos(6*y*pi)*cos(2*z*pi) + 8*cos(6*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA311*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB311 = - 8*sin(2*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 8*sin(2*x*pi)*sin(6*y*pi)*sin(2*z*pi) - 8*sin(6*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB311*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,1])
        idx_a += 1

    if 11 in usedBasis:
        fA222 = 24*cos(4*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA222*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB222 = -24*sin(4*x*pi)*sin(4*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB222*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,2])
        idx_a += 1

    if 12 in usedBasis:
        fA320 = 4*cos(4*x*pi)*cos(6*y*pi) + 4*cos(6*x*pi)*cos(4*y*pi) + 4*cos(4*x*pi)*cos(6*z*pi) + 4*cos(6*x*pi)*cos(4*z*pi) + 4*cos(4*y*pi)*cos(6*z*pi) + 4*cos(6*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA320*Multi[idx_a]
        hkl.append([3,2,0])
        idx_a += 1

    if 13 in usedBasis:
        fA321 = 4*cos(2*x*pi)*cos(4*y*pi)*cos(6*z*pi) + 4*cos(2*x*pi)*cos(6*y*pi)*cos(4*z*pi) + 4*cos(4*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 4*cos(4*x*pi)*cos(6*y*pi)*cos(2*z*pi) + 4*cos(6*x*pi)*cos(2*y*pi)*cos(4*z*pi) + 4*cos(6*x*pi)*cos(4*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA321*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB321 = - 4*sin(2*x*pi)*sin(4*y*pi)*sin(6*z*pi) - 4*sin(2*x*pi)*sin(6*y*pi)*sin(4*z*pi) - 4*sin(4*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 4*sin(4*x*pi)*sin(6*y*pi)*sin(2*z*pi) - 4*sin(6*x*pi)*sin(2*y*pi)*sin(4*z*pi) - 4*sin(6*x*pi)*sin(4*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB321*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,1])
        idx_a += 1

    if 14 in usedBasis:
        fA400 = 8*cos(8*x*pi) + 8*cos(8*y*pi) + 8*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 15 in usedBasis:
        fA322 = 8*cos(4*x*pi)*cos(4*y*pi)*cos(6*z*pi) + 8*cos(4*x*pi)*cos(6*y*pi)*cos(4*z*pi) + 8*cos(6*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA322*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB322 = - 8*sin(4*x*pi)*sin(4*y*pi)*sin(6*z*pi) - 8*sin(4*x*pi)*sin(6*y*pi)*sin(4*z*pi) - 8*sin(6*x*pi)*sin(4*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB322*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,2])
        idx_a += 1

    if 16 in usedBasis:
        fA410 = 4*cos(2*x*pi)*cos(8*y*pi) + 4*cos(8*x*pi)*cos(2*y*pi) + 4*cos(2*x*pi)*cos(8*z*pi) + 4*cos(8*x*pi)*cos(2*z*pi) + 4*cos(2*y*pi)*cos(8*z*pi) + 4*cos(8*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA410*Multi[idx_a]
        hkl.append([4,1,0])
        idx_a += 1

    if 17 in usedBasis:
        fA330 = 8*cos(6*x*pi)*cos(6*y*pi) + 8*cos(6*x*pi)*cos(6*z*pi) + 8*cos(6*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA330*Multi[idx_a]
        hkl.append([3,3,0])
        idx_a += 1

    if 18 in usedBasis:
        fA411 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(8*z*pi) + 8*cos(2*x*pi)*cos(8*y*pi)*cos(2*z*pi) + 8*cos(8*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA411*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB411 = - 8*sin(2*x*pi)*sin(2*y*pi)*sin(8*z*pi) - 8*sin(2*x*pi)*sin(8*y*pi)*sin(2*z*pi) - 8*sin(8*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB411*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,1,1])
        idx_a += 1

    if 19 in usedBasis:
        fA331 = 8*cos(2*x*pi)*cos(6*y*pi)*cos(6*z*pi) + 8*cos(6*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 8*cos(6*x*pi)*cos(6*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA331*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB331 = - 8*sin(2*x*pi)*sin(6*y*pi)*sin(6*z*pi) - 8*sin(6*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 8*sin(6*x*pi)*sin(6*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB331*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,3,1])
        idx_a += 1

    if 20 in usedBasis:
        fA420 = 4*cos(4*x*pi)*(2*cos(4*y*pi)**2 - 1) + 4*cos(4*y*pi)*(2*cos(4*x*pi)**2 - 1) + 4*cos(4*x*pi)*(2*cos(4*z*pi)**2 - 1) + 4*cos(4*z*pi)*(2*cos(4*x*pi)**2 - 1) + 4*cos(4*y*pi)*(2*cos(4*z*pi)**2 - 1) + 4*cos(4*z*pi)*(2*cos(4*y*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA420*Multi[idx_a]
        hkl.append([4,2,0])
        idx_a += 1

    if 21 in usedBasis:
        fA421 = 4*cos(2*x*pi)*cos(4*y*pi)*cos(8*z*pi) + 4*cos(2*x*pi)*cos(8*y*pi)*cos(4*z*pi) + 4*cos(4*x*pi)*cos(2*y*pi)*cos(8*z*pi) + 4*cos(4*x*pi)*cos(8*y*pi)*cos(2*z*pi) + 4*cos(8*x*pi)*cos(2*y*pi)*cos(4*z*pi) + 4*cos(8*x*pi)*cos(4*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA421*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB421 = - 4*sin(2*x*pi)*sin(4*y*pi)*sin(8*z*pi) - 4*sin(2*x*pi)*sin(8*y*pi)*sin(4*z*pi) - 4*sin(4*x*pi)*sin(2*y*pi)*sin(8*z*pi) - 4*sin(4*x*pi)*sin(8*y*pi)*sin(2*z*pi) - 4*sin(8*x*pi)*sin(2*y*pi)*sin(4*z*pi) - 4*sin(8*x*pi)*sin(4*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB421*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,2,1])
        idx_a += 1

    if 22 in usedBasis:
        fA332 = 8*cos(4*x*pi)*cos(6*y*pi)*cos(6*z*pi) + 8*cos(6*x*pi)*cos(4*y*pi)*cos(6*z*pi) + 8*cos(6*x*pi)*cos(6*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA332*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB332 = - 8*sin(4*x*pi)*sin(6*y*pi)*sin(6*z*pi) - 8*sin(6*x*pi)*sin(4*y*pi)*sin(6*z*pi) - 8*sin(6*x*pi)*sin(6*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB332*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,3,2])
        idx_a += 1

    if 23 in usedBasis:
        fA422 = 8*cos(4*x*pi)*cos(4*y*pi)*(2*cos(4*z*pi)**2 - 1) + 8*cos(4*x*pi)*cos(4*z*pi)*(2*cos(4*y*pi)**2 - 1) + 8*cos(4*y*pi)*cos(4*z*pi)*(2*cos(4*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA422*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB422 = - 8*sin(4*x*pi)*sin(4*y*pi)*sin(8*z*pi) - 8*sin(4*x*pi)*sin(8*y*pi)*sin(4*z*pi) - 8*sin(8*x*pi)*sin(4*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB422*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,2,2])
        idx_a += 1

    if 24 in usedBasis:
        fA430 = 4*cos(6*x*pi)*cos(8*y*pi) + 4*cos(8*x*pi)*cos(6*y*pi) + 4*cos(6*x*pi)*cos(8*z*pi) + 4*cos(8*x*pi)*cos(6*z*pi) + 4*cos(6*y*pi)*cos(8*z*pi) + 4*cos(8*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA430*Multi[idx_a]
        hkl.append([4,3,0])
        idx_a += 1

    if 25 in usedBasis:
        fA500 = 8*cos(10*x*pi) + 8*cos(10*y*pi) + 8*cos(10*z*pi)
        FA += SF.ai[idx_a]*fA500*Multi[idx_a]
        hkl.append([5,0,0])
        idx_a += 1

    if 26 in usedBasis:
        fA431 = 4*cos(2*x*pi)*cos(6*y*pi)*cos(8*z*pi) + 4*cos(2*x*pi)*cos(8*y*pi)*cos(6*z*pi) + 4*cos(6*x*pi)*cos(2*y*pi)*cos(8*z*pi) + 4*cos(6*x*pi)*cos(8*y*pi)*cos(2*z*pi) + 4*cos(8*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 4*cos(8*x*pi)*cos(6*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA431*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB431 = - 4*sin(2*x*pi)*sin(6*y*pi)*sin(8*z*pi) - 4*sin(2*x*pi)*sin(8*y*pi)*sin(6*z*pi) - 4*sin(6*x*pi)*sin(2*y*pi)*sin(8*z*pi) - 4*sin(6*x*pi)*sin(8*y*pi)*sin(2*z*pi) - 4*sin(8*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 4*sin(8*x*pi)*sin(6*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB431*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,3,1])
        idx_a += 1

    if 27 in usedBasis:
        fA510 = 4*cos(2*x*pi)*cos(10*y*pi) + 4*cos(10*x*pi)*cos(2*y*pi) + 4*cos(2*x*pi)*cos(10*z*pi) + 4*cos(10*x*pi)*cos(2*z*pi) + 4*cos(2*y*pi)*cos(10*z*pi) + 4*cos(10*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA510*Multi[idx_a]
        hkl.append([5,1,0])
        idx_a += 1

    if 28 in usedBasis:
        fA333 = 24*cos(6*x*pi)*cos(6*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA333*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB333 = -24*sin(6*x*pi)*sin(6*y*pi)*sin(6*z*pi)
        FB += SF.ai[idx_a]*fB333*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,3,3])
        idx_a += 1

    if 29 in usedBasis:
        fA511 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(10*z*pi) + 8*cos(2*x*pi)*cos(10*y*pi)*cos(2*z*pi) + 8*cos(10*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA511*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB511 = - 8*sin(2*x*pi)*sin(2*y*pi)*sin(10*z*pi) - 8*sin(2*x*pi)*sin(10*y*pi)*sin(2*z*pi) - 8*sin(10*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB511*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,1,1])
        idx_a += 1

    if 30 in usedBasis:
        fA432 = 4*cos(4*x*pi)*cos(6*y*pi)*(2*cos(4*z*pi)**2 - 1) + 4*cos(4*x*pi)*cos(6*z*pi)*(2*cos(4*y*pi)**2 - 1) + 4*cos(6*x*pi)*cos(4*y*pi)*(2*cos(4*z*pi)**2 - 1) + 4*cos(6*x*pi)*cos(4*z*pi)*(2*cos(4*y*pi)**2 - 1) + 4*cos(4*y*pi)*cos(6*z*pi)*(2*cos(4*x*pi)**2 - 1) + 4*cos(6*y*pi)*cos(4*z*pi)*(2*cos(4*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA432*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB432 = - 4*sin(4*x*pi)*sin(6*y*pi)*sin(8*z*pi) - 4*sin(4*x*pi)*sin(8*y*pi)*sin(6*z*pi) - 4*sin(6*x*pi)*sin(4*y*pi)*sin(8*z*pi) - 4*sin(6*x*pi)*sin(8*y*pi)*sin(4*z*pi) - 4*sin(8*x*pi)*sin(4*y*pi)*sin(6*z*pi) - 4*sin(8*x*pi)*sin(6*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB432*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,3,2])
        idx_a += 1

    if 31 in usedBasis:
        fA520 = 4*cos(4*x*pi)*cos(10*y*pi) + 4*cos(10*x*pi)*cos(4*y*pi) + 4*cos(4*x*pi)*cos(10*z*pi) + 4*cos(10*x*pi)*cos(4*z*pi) + 4*cos(4*y*pi)*cos(10*z*pi) + 4*cos(10*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA520*Multi[idx_a]
        hkl.append([5,2,0])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 1 0 0 1 0 1 0 0 1 1 0 1 0 1 0 0 1 1 0 1 1 1 0 0 1 0 1 1 1 0 
    # 215: [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
    return FA+FB, idx_theta, hkl
