# Generated at 2024-02-23 21:44:30
# Qingshu Dong

import numpy as np

def  calF_142(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([4, 16, 8, 4, 8, 16, 16, 16, 4, 2, 16, 8, 8, 8, 8, 16, 16, 8, 16, 16, 16, 16, 16, 16, 4, 8, 16, 4, 16, 16, 16, 16])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 142.2')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA200 = 16*cos(4*x*pi) - 16*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 1 in usedBasis:
        fA211 = - 16*cos(2*y*pi)*sin(4*x*pi)*sin(2*z*pi) - 16*cos(2*z*pi)*sin(2*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA211*Multi[idx_a]
        hkl.append([2,1,1])
        idx_a += 1

    if 2 in usedBasis:
        fA112 = -32*cos(2*x*pi)*sin(2*y*pi)*sin(4*z*pi)
        FA += SF.ai[idx_a]*fA112*Multi[idx_a]
        hkl.append([1,1,2])
        idx_a += 1

    if 3 in usedBasis:
        fA220 = 32*cos(4*x*pi)*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 4 in usedBasis:
        fA202 = 16*cos(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA202*Multi[idx_a]
        hkl.append([2,0,2])
        idx_a += 1

    if 5 in usedBasis:
        fA321 = 16*cos(6*y*pi)*sin(4*x*pi)*sin(2*z*pi) - 16*cos(2*z*pi)*sin(6*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA321*Multi[idx_a]
        hkl.append([3,2,1])
        idx_a += 1

    if 6 in usedBasis:
        fA312 = 16*sin(4*z*pi)*(cos(2*x*pi)*sin(6*y*pi) - cos(6*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA312*Multi[idx_a]
        hkl.append([3,1,2])
        idx_a += 1

    if 7 in usedBasis:
        fA213 = 16*cos(6*z*pi)*sin(2*x*pi)*sin(4*y*pi) - 16*cos(2*y*pi)*sin(4*x*pi)*sin(6*z*pi)
        FA += SF.ai[idx_a]*fA213*Multi[idx_a]
        hkl.append([2,1,3])
        idx_a += 1

    if 8 in usedBasis:
        fA400 = 16*cos(8*x*pi) + 16*cos(8*y*pi)
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 9 in usedBasis:
        fA004 = 32*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA004*Multi[idx_a]
        hkl.append([0,0,4])
        idx_a += 1

    if 10 in usedBasis:
        fA411 = 16*cos(2*z*pi)*sin(2*x*pi)*sin(8*y*pi) - 16*cos(2*y*pi)*sin(8*x*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA411*Multi[idx_a]
        hkl.append([4,1,1])
        idx_a += 1

    if 11 in usedBasis:
        fA420 = 16*cos(4*y*pi)*(2*cos(4*x*pi)**2 - 1) - 16*cos(4*x*pi)*(2*cos(4*y*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA420*Multi[idx_a]
        hkl.append([4,2,0])
        idx_a += 1

    if 12 in usedBasis:
        fA402 = 16*cos(4*z*pi)*(cos(8*x*pi) - cos(8*y*pi))
        FA += SF.ai[idx_a]*fA402*Multi[idx_a]
        hkl.append([4,0,2])
        idx_a += 1

    if 13 in usedBasis:
        fA204 = 16*cos(8*z*pi)*(cos(4*x*pi) - cos(4*y*pi))
        FA += SF.ai[idx_a]*fA204*Multi[idx_a]
        hkl.append([2,0,4])
        idx_a += 1

    if 14 in usedBasis:
        fA332 = -32*cos(6*x*pi)*sin(6*y*pi)*sin(4*z*pi)
        FA += SF.ai[idx_a]*fA332*Multi[idx_a]
        hkl.append([3,3,2])
        idx_a += 1

    if 15 in usedBasis:
        fA323 = - 16*cos(6*y*pi)*sin(4*x*pi)*sin(6*z*pi) - 16*cos(6*z*pi)*sin(6*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA323*Multi[idx_a]
        hkl.append([3,2,3])
        idx_a += 1

    if 16 in usedBasis:
        fA422 = 16*cos(4*x*pi)*cos(4*z*pi)*(2*cos(4*y*pi)**2 - 1) + 16*cos(4*y*pi)*cos(4*z*pi)*(2*cos(4*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA422*Multi[idx_a]
        hkl.append([4,2,2])
        idx_a += 1

    if 17 in usedBasis:
        fA224 = 32*cos(4*x*pi)*cos(4*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA224*Multi[idx_a]
        hkl.append([2,2,4])
        idx_a += 1

    if 18 in usedBasis:
        fA431 = - 16*cos(6*y*pi)*sin(8*x*pi)*sin(2*z*pi) - 16*cos(2*z*pi)*sin(6*x*pi)*sin(8*y*pi)
        FA += SF.ai[idx_a]*fA431*Multi[idx_a]
        hkl.append([4,3,1])
        idx_a += 1

    if 19 in usedBasis:
        fA413 = - 16*cos(2*y*pi)*sin(8*x*pi)*sin(6*z*pi) - 16*cos(6*z*pi)*sin(2*x*pi)*sin(8*y*pi)
        FA += SF.ai[idx_a]*fA413*Multi[idx_a]
        hkl.append([4,1,3])
        idx_a += 1

    if 20 in usedBasis:
        fA314 = -16*sin(8*z*pi)*(cos(2*x*pi)*sin(6*y*pi) + cos(6*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA314*Multi[idx_a]
        hkl.append([3,1,4])
        idx_a += 1

    if 21 in usedBasis:
        fA521 = - 16*cos(10*y*pi)*sin(4*x*pi)*sin(2*z*pi) - 16*cos(2*z*pi)*sin(10*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA521*Multi[idx_a]
        hkl.append([5,2,1])
        idx_a += 1

    if 22 in usedBasis:
        fA512 = -16*sin(4*z*pi)*(cos(2*x*pi)*sin(10*y*pi) + cos(10*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA512*Multi[idx_a]
        hkl.append([5,1,2])
        idx_a += 1

    if 23 in usedBasis:
        fA215 = - 16*cos(2*y*pi)*sin(4*x*pi)*sin(10*z*pi) - 16*cos(10*z*pi)*sin(2*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA215*Multi[idx_a]
        hkl.append([2,1,5])
        idx_a += 1

    if 24 in usedBasis:
        fA440 = 32*cos(8*x*pi)*cos(8*y*pi)
        FA += SF.ai[idx_a]*fA440*Multi[idx_a]
        hkl.append([4,4,0])
        idx_a += 1

    if 25 in usedBasis:
        fA404 = 16*cos(8*z*pi)*(cos(8*x*pi) + cos(8*y*pi))
        FA += SF.ai[idx_a]*fA404*Multi[idx_a]
        hkl.append([4,0,4])
        idx_a += 1

    if 26 in usedBasis:
        fA433 = 16*cos(6*z*pi)*sin(6*x*pi)*sin(8*y*pi) - 16*cos(6*y*pi)*sin(8*x*pi)*sin(6*z*pi)
        FA += SF.ai[idx_a]*fA433*Multi[idx_a]
        hkl.append([4,3,3])
        idx_a += 1

    if 27 in usedBasis:
        fA600 = 16*cos(12*x*pi) - 16*cos(12*y*pi)
        FA += SF.ai[idx_a]*fA600*Multi[idx_a]
        hkl.append([6,0,0])
        idx_a += 1

    if 28 in usedBasis:
        fA424 = 16*cos(4*y*pi)*cos(8*z*pi)*(2*cos(4*x*pi)**2 - 1) - 16*cos(4*x*pi)*cos(8*z*pi)*(2*cos(4*y*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA424*Multi[idx_a]
        hkl.append([4,2,4])
        idx_a += 1

    if 29 in usedBasis:
        fA611 = - 16*cos(2*y*pi)*sin(12*x*pi)*sin(2*z*pi) - 16*cos(2*z*pi)*sin(2*x*pi)*sin(12*y*pi)
        FA += SF.ai[idx_a]*fA611*Multi[idx_a]
        hkl.append([6,1,1])
        idx_a += 1

    if 30 in usedBasis:
        fA532 = 16*sin(4*z*pi)*(cos(6*x*pi)*sin(10*y*pi) - cos(10*x*pi)*sin(6*y*pi))
        FA += SF.ai[idx_a]*fA532*Multi[idx_a]
        hkl.append([5,3,2])
        idx_a += 1

    if 31 in usedBasis:
        fA523 = 16*cos(10*y*pi)*sin(4*x*pi)*sin(6*z*pi) - 16*cos(6*z*pi)*sin(10*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA523*Multi[idx_a]
        hkl.append([5,2,3])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    # 142: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return FA+FB, idx_theta, hkl
