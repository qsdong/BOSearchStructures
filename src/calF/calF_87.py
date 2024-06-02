# Generated at 2024-02-23 21:06:22
# Qingshu Dong

import numpy as np

def  calF_87(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([4, 8, 4, 2, 16, 8, 4, 8, 8, 8, 8, 8, 16, 16, 16, 4, 2, 4, 16, 8, 8, 8, 8, 8, 8, 16, 16, 8, 8, 16, 8, 16])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 87.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA110 = 16*cos(2*x*pi)*cos(2*y*pi)
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 1 in usedBasis:
        fA101 = 8*cos(2*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA101*Multi[idx_a]
        hkl.append([1,0,1])
        idx_a += 1

    if 2 in usedBasis:
        fA200 = 8*cos(4*x*pi) + 8*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 3 in usedBasis:
        fA002 = 16*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA002*Multi[idx_a]
        hkl.append([0,0,2])
        idx_a += 1

    if 4 in usedBasis:
        fA211 = 8*cos(2*z*pi)*(cos(2*pi*(x - 2*y)) + cos(2*pi*(2*x + y)))
        FA += SF.ai[idx_a]*fA211*Multi[idx_a]
        hkl.append([2,1,1])
        idx_a += 1

    if 5 in usedBasis:
        fA112 = 16*cos(2*x*pi)*cos(2*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA112*Multi[idx_a]
        hkl.append([1,1,2])
        idx_a += 1

    if 6 in usedBasis:
        fA220 = 16*cos(4*x*pi)*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 7 in usedBasis:
        fA202 = 8*cos(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA202*Multi[idx_a]
        hkl.append([2,0,2])
        idx_a += 1

    if 8 in usedBasis:
        fA310 = 8*cos(2*pi*(x - 3*y)) + 8*cos(2*pi*(3*x + y))
        FA += SF.ai[idx_a]*fA310*Multi[idx_a]
        hkl.append([3,1,0])
        idx_a += 1

    if 9 in usedBasis:
        fA301 = 8*cos(2*z*pi)*(cos(6*x*pi) + cos(6*y*pi))
        FA += SF.ai[idx_a]*fA301*Multi[idx_a]
        hkl.append([3,0,1])
        idx_a += 1

    if 10 in usedBasis:
        fA103 = 8*cos(6*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA103*Multi[idx_a]
        hkl.append([1,0,3])
        idx_a += 1

    if 11 in usedBasis:
        fA222 = 16*cos(4*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA222*Multi[idx_a]
        hkl.append([2,2,2])
        idx_a += 1

    if 12 in usedBasis:
        fA321 = 8*cos(2*z*pi)*(cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x + 2*y)))
        FA += SF.ai[idx_a]*fA321*Multi[idx_a]
        hkl.append([3,2,1])
        idx_a += 1

    if 13 in usedBasis:
        fA312 = 8*cos(4*z*pi)*(cos(2*pi*(x - 3*y)) + cos(2*pi*(3*x + y)))
        FA += SF.ai[idx_a]*fA312*Multi[idx_a]
        hkl.append([3,1,2])
        idx_a += 1

    if 14 in usedBasis:
        fA213 = 8*cos(6*z*pi)*(cos(2*pi*(x - 2*y)) + cos(2*pi*(2*x + y)))
        FA += SF.ai[idx_a]*fA213*Multi[idx_a]
        hkl.append([2,1,3])
        idx_a += 1

    if 15 in usedBasis:
        fA400 = 8*cos(8*x*pi) + 8*cos(8*y*pi)
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 16 in usedBasis:
        fA004 = 16*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA004*Multi[idx_a]
        hkl.append([0,0,4])
        idx_a += 1

    if 17 in usedBasis:
        fA330 = 16*cos(6*x*pi)*cos(6*y*pi)
        FA += SF.ai[idx_a]*fA330*Multi[idx_a]
        hkl.append([3,3,0])
        idx_a += 1

    if 18 in usedBasis:
        fA411 = 8*cos(2*z*pi)*(cos(2*pi*(x - 4*y)) + cos(2*pi*(4*x + y)))
        FA += SF.ai[idx_a]*fA411*Multi[idx_a]
        hkl.append([4,1,1])
        idx_a += 1

    if 19 in usedBasis:
        fA303 = 8*cos(6*z*pi)*(cos(6*x*pi) + cos(6*y*pi))
        FA += SF.ai[idx_a]*fA303*Multi[idx_a]
        hkl.append([3,0,3])
        idx_a += 1

    if 20 in usedBasis:
        fA114 = 16*cos(2*x*pi)*cos(2*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA114*Multi[idx_a]
        hkl.append([1,1,4])
        idx_a += 1

    if 21 in usedBasis:
        fA420 = 8*cos(4*pi*(x - 2*y)) + 8*cos(4*pi*(2*x + y))
        FA += SF.ai[idx_a]*fA420*Multi[idx_a]
        hkl.append([4,2,0])
        idx_a += 1

    if 22 in usedBasis:
        fA402 = 8*cos(4*z*pi)*(cos(8*x*pi) + cos(8*y*pi))
        FA += SF.ai[idx_a]*fA402*Multi[idx_a]
        hkl.append([4,0,2])
        idx_a += 1

    if 23 in usedBasis:
        fA204 = 8*cos(8*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA204*Multi[idx_a]
        hkl.append([2,0,4])
        idx_a += 1

    if 24 in usedBasis:
        fA332 = 16*cos(6*x*pi)*cos(6*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA332*Multi[idx_a]
        hkl.append([3,3,2])
        idx_a += 1

    if 25 in usedBasis:
        fA323 = 8*cos(6*z*pi)*(cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x + 2*y)))
        FA += SF.ai[idx_a]*fA323*Multi[idx_a]
        hkl.append([3,2,3])
        idx_a += 1

    if 26 in usedBasis:
        fA422 = 8*cos(4*z*pi)*(cos(4*pi*(x - 2*y)) + cos(4*pi*(2*x + y)))
        FA += SF.ai[idx_a]*fA422*Multi[idx_a]
        hkl.append([4,2,2])
        idx_a += 1

    if 27 in usedBasis:
        fA224 = 16*cos(4*x*pi)*cos(4*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA224*Multi[idx_a]
        hkl.append([2,2,4])
        idx_a += 1

    if 28 in usedBasis:
        fA510 = 8*cos(2*pi*(x - 5*y)) + 8*cos(2*pi*(5*x + y))
        FA += SF.ai[idx_a]*fA510*Multi[idx_a]
        hkl.append([5,1,0])
        idx_a += 1

    if 29 in usedBasis:
        fA431 = 8*cos(2*z*pi)*(cos(2*pi*(3*x - 4*y)) + cos(2*pi*(4*x + 3*y)))
        FA += SF.ai[idx_a]*fA431*Multi[idx_a]
        hkl.append([4,3,1])
        idx_a += 1

    if 30 in usedBasis:
        fA501 = 8*cos(2*z*pi)*(cos(10*x*pi) + cos(10*y*pi))
        FA += SF.ai[idx_a]*fA501*Multi[idx_a]
        hkl.append([5,0,1])
        idx_a += 1

    if 31 in usedBasis:
        fA413 = 8*cos(6*z*pi)*(cos(2*pi*(x - 4*y)) + cos(2*pi*(4*x + y)))
        FA += SF.ai[idx_a]*fA413*Multi[idx_a]
        hkl.append([4,1,3])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    # 87: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return FA+FB, idx_theta, hkl
