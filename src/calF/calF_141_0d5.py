# Generated at 2024-02-26 10:43:03
# Qingshu Dong

import numpy as np

def  calF_141_0d5(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([4, 8, 4, 16, 8, 4, 16, 8, 8, 8, 16, 16, 16, 8, 4, 8, 16, 8, 4, 16, 8, 8, 16, 16, 16, 16, 8, 16, 16, 16, 8, 8])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 141.2')

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
        fA101 = 16*cos(2*x*pi)*cos(2*z*pi) - 16*sin(2*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA101*Multi[idx_a]
        hkl.append([1,0,1])
        idx_a += 1

    if 2 in usedBasis:
        fA220 = 32*cos(4*x*pi)*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 3 in usedBasis:
        fA211 = - 16*cos(2*x*pi)*cos(2*z*pi)*(2*cos(2*y*pi)**2 - 1) - 16*sin(2*y*pi)*sin(2*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA211*Multi[idx_a]
        hkl.append([2,1,1])
        idx_a += 1

    if 4 in usedBasis:
        fA301 = 16*cos(6*x*pi)*cos(2*z*pi) + 16*sin(6*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA301*Multi[idx_a]
        hkl.append([3,0,1])
        idx_a += 1

    if 5 in usedBasis:
        fA400 = 16*cos(8*x*pi) + 16*cos(8*y*pi)
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 6 in usedBasis:
        fA321 = 16*cos(6*x*pi)*cos(4*y*pi)*cos(2*z*pi) - 16*cos(4*x*pi)*sin(6*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA321*Multi[idx_a]
        hkl.append([3,2,1])
        idx_a += 1

    if 7 in usedBasis:
        fA112 = -32*cos(2*x*pi)*sin(2*y*pi)*sin(4*z*pi)
        FA += SF.ai[idx_a]*fA112*Multi[idx_a]
        hkl.append([1,1,2])
        idx_a += 1

    if 8 in usedBasis:
        fA420 = 16*cos(4*y*pi)*(2*cos(4*x*pi)**2 - 1) - 16*cos(4*x*pi)*(2*cos(4*y*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA420*Multi[idx_a]
        hkl.append([4,2,0])
        idx_a += 1

    if 9 in usedBasis:
        fA202 = 16*cos(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA202*Multi[idx_a]
        hkl.append([2,0,2])
        idx_a += 1

    if 10 in usedBasis:
        fA411 = 16*cos(2*x*pi)*cos(8*y*pi)*cos(2*z*pi) - 16*cos(8*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA411*Multi[idx_a]
        hkl.append([4,1,1])
        idx_a += 1

    if 11 in usedBasis:
        fA312 = 16*sin(4*z*pi)*(cos(2*x*pi)*sin(6*y*pi) - cos(6*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA312*Multi[idx_a]
        hkl.append([3,1,2])
        idx_a += 1

    if 12 in usedBasis:
        fA431 = - 16*cos(6*x*pi)*cos(8*y*pi)*cos(2*z*pi) - 16*cos(8*x*pi)*sin(6*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA431*Multi[idx_a]
        hkl.append([4,3,1])
        idx_a += 1

    if 13 in usedBasis:
        fA501 = 16*cos(10*x*pi)*cos(2*z*pi) - 16*sin(10*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA501*Multi[idx_a]
        hkl.append([5,0,1])
        idx_a += 1

    if 14 in usedBasis:
        fA440 = 32*cos(8*x*pi)*cos(8*y*pi)
        FA += SF.ai[idx_a]*fA440*Multi[idx_a]
        hkl.append([4,4,0])
        idx_a += 1

    if 15 in usedBasis:
        fA402 = 16*cos(4*z*pi)*(cos(8*x*pi) - cos(8*y*pi))
        FA += SF.ai[idx_a]*fA402*Multi[idx_a]
        hkl.append([4,0,2])
        idx_a += 1

    if 16 in usedBasis:
        fA521 = 16*cos(10*x*pi)*cos(4*y*pi)*cos(2*z*pi) + 16*cos(4*x*pi)*sin(10*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA521*Multi[idx_a]
        hkl.append([5,2,1])
        idx_a += 1

    if 17 in usedBasis:
        fA332 = -32*cos(6*x*pi)*sin(6*y*pi)*sin(4*z*pi)
        FA += SF.ai[idx_a]*fA332*Multi[idx_a]
        hkl.append([3,3,2])
        idx_a += 1

    if 18 in usedBasis:
        fA600 = 16*cos(12*x*pi) - 16*cos(12*y*pi)
        FA += SF.ai[idx_a]*fA600*Multi[idx_a]
        hkl.append([6,0,0])
        idx_a += 1

    if 19 in usedBasis:
        fA422 = 16*cos(4*x*pi)*cos(4*z*pi)*(2*cos(4*y*pi)**2 - 1) + 16*cos(4*y*pi)*cos(4*z*pi)*(2*cos(4*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA422*Multi[idx_a]
        hkl.append([4,2,2])
        idx_a += 1

    if 20 in usedBasis:
        fA103 = 16*cos(2*x*pi)*cos(6*z*pi) + 16*sin(2*y*pi)*sin(6*z*pi)
        FA += SF.ai[idx_a]*fA103*Multi[idx_a]
        hkl.append([1,0,3])
        idx_a += 1

    if 21 in usedBasis:
        fA620 = 32*cos(4*x*pi)*cos(4*y*pi)*(2*cos(4*x*pi)**2 + 2*cos(4*y*pi)**2 - 3)
        FA += SF.ai[idx_a]*fA620*Multi[idx_a]
        hkl.append([6,2,0])
        idx_a += 1

    if 22 in usedBasis:
        fA611 = - 16*cos(2*x*pi)*cos(12*y*pi)*cos(2*z*pi) - 16*cos(12*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA611*Multi[idx_a]
        hkl.append([6,1,1])
        idx_a += 1

    if 23 in usedBasis:
        fA213 = 16*cos(2*x*pi)*cos(6*z*pi)*(2*cos(2*y*pi)**2 - 1) - 16*sin(2*y*pi)*sin(6*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA213*Multi[idx_a]
        hkl.append([2,1,3])
        idx_a += 1

    if 24 in usedBasis:
        fA512 = -16*sin(4*z*pi)*(cos(2*x*pi)*sin(10*y*pi) + cos(10*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA512*Multi[idx_a]
        hkl.append([5,1,2])
        idx_a += 1

    if 25 in usedBasis:
        fA541 = 16*cos(10*x*pi)*cos(8*y*pi)*cos(2*z*pi) - 16*cos(8*x*pi)*sin(10*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA541*Multi[idx_a]
        hkl.append([5,4,1])
        idx_a += 1

    if 26 in usedBasis:
        fA303 = 16*cos(6*x*pi)*cos(6*z*pi) - 16*sin(6*y*pi)*sin(6*z*pi)
        FA += SF.ai[idx_a]*fA303*Multi[idx_a]
        hkl.append([3,0,3])
        idx_a += 1

    if 27 in usedBasis:
        fA631 = 16*cos(6*x*pi)*cos(2*z*pi)*(2*cos(6*y*pi)**2 - 1) - 16*sin(6*y*pi)*sin(2*z*pi)*(2*cos(6*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA631*Multi[idx_a]
        hkl.append([6,3,1])
        idx_a += 1

    if 28 in usedBasis:
        fA323 = 16*cos(6*x*pi)*cos(4*y*pi)*cos(6*z*pi) + 16*cos(4*x*pi)*sin(6*y*pi)*sin(6*z*pi)
        FA += SF.ai[idx_a]*fA323*Multi[idx_a]
        hkl.append([3,2,3])
        idx_a += 1

    if 29 in usedBasis:
        fA532 = 16*sin(4*z*pi)*(cos(6*x*pi)*sin(10*y*pi) - cos(10*x*pi)*sin(6*y*pi))
        FA += SF.ai[idx_a]*fA532*Multi[idx_a]
        hkl.append([5,3,2])
        idx_a += 1

    if 30 in usedBasis:
        fA640 = 16*cos(12*x*pi)*cos(8*y*pi) - 16*cos(8*x*pi)*cos(12*y*pi)
        FA += SF.ai[idx_a]*fA640*Multi[idx_a]
        hkl.append([6,4,0])
        idx_a += 1

    if 31 in usedBasis:
        fA602 = 16*cos(4*z*pi)*(cos(12*x*pi) + cos(12*y*pi))
        FA += SF.ai[idx_a]*fA602*Multi[idx_a]
        hkl.append([6,0,2])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    # 141_0d5: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return FA+FB, idx_theta, hkl
