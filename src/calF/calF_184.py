# Generated at 2024-02-23 17:34:59
# Qingshu Dong

import numpy as np

def  calF_184(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([6, 6, 2, 6, 12, 12, 12, 12, 24, 6, 24, 6, 12, 2, 12, 12, 24, 24, 12, 12, 6, 24, 12, 12, 12, 24, 24, 24, 12, 12, 24, 24])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 184.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA100 = 4*cos(2*x*pi) + 4*cos(2*y*pi) + 4*cos(2*pi*(x - y))
        FA += SF.ai[idx_a]*fA100*Multi[idx_a]
        hkl.append([1,0,0])
        idx_a += 1

    if 1 in usedBasis:
        fA110 = 4*cos(2*pi*(2*x - y)) + 4*cos(2*pi*(x + y)) + 4*cos(2*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 2 in usedBasis:
        fA002 = 12*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA002*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB002 = 12*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB002*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,2])
        idx_a += 1

    if 3 in usedBasis:
        fA200 = 4*cos(4*x*pi) + 4*cos(4*y*pi) + 4*cos(4*pi*(x - y))
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 4 in usedBasis:
        fA102 = 4*cos(4*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA102*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB102 = 4*sin(4*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FB += SF.ai[idx_a]*fB102*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,2])
        idx_a += 1

    if 5 in usedBasis:
        fA112 = 4*cos(4*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA112*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB112 = 4*sin(4*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB112*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,2])
        idx_a += 1

    if 6 in usedBasis:
        fA210 = 2*cos(2*pi*(3*x - y)) + 2*cos(2*pi*(2*x - 3*y)) + 2*cos(2*pi*(3*x - 2*y)) + 2*cos(2*pi*(x + 2*y)) + 2*cos(2*pi*(2*x + y)) + 2*cos(2*pi*(x - 3*y))
        FA += SF.ai[idx_a]*fA210*Multi[idx_a]
        hkl.append([2,1,0])
        idx_a += 1

    if 7 in usedBasis:
        fA202 = 4*cos(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA202*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB202 = 4*sin(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FB += SF.ai[idx_a]*fB202*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,2])
        idx_a += 1

    if 8 in usedBasis:
        fA211 = -2*cos(2*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) - cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) - cos(2*pi*(2*x + y)) - cos(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = -2*sin(2*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) - cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) - cos(2*pi*(2*x + y)) - cos(2*pi*(x - 3*y)))
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 9 in usedBasis:
        fA300 = 4*cos(6*x*pi) + 4*cos(6*y*pi) + 4*cos(6*pi*(x - y))
        FA += SF.ai[idx_a]*fA300*Multi[idx_a]
        hkl.append([3,0,0])
        idx_a += 1

    if 10 in usedBasis:
        fA212 = 2*cos(4*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA212*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB212 = 2*sin(4*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FB += SF.ai[idx_a]*fB212*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,2])
        idx_a += 1

    if 11 in usedBasis:
        fA220 = 4*cos(4*pi*(2*x - y)) + 4*cos(4*pi*(x + y)) + 4*cos(4*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 12 in usedBasis:
        fA302 = 4*cos(4*z*pi)*(cos(6*x*pi) + cos(6*y*pi) + cos(6*pi*(x - y)))
        FA += SF.ai[idx_a]*fA302*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB302 = 4*sin(4*z*pi)*(cos(6*x*pi) + cos(6*y*pi) + cos(6*pi*(x - y)))
        FB += SF.ai[idx_a]*fB302*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,2])
        idx_a += 1

    if 13 in usedBasis:
        fA004 = 12*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA004*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB004 = 12*sin(8*z*pi)
        FB += SF.ai[idx_a]*fB004*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,4])
        idx_a += 1

    if 14 in usedBasis:
        fA310 = 2*cos(2*pi*(4*x - y)) + 2*cos(2*pi*(3*x - 4*y)) + 2*cos(2*pi*(4*x - 3*y)) + 2*cos(2*pi*(x + 3*y)) + 2*cos(2*pi*(3*x + y)) + 2*cos(2*pi*(x - 4*y))
        FA += SF.ai[idx_a]*fA310*Multi[idx_a]
        hkl.append([3,1,0])
        idx_a += 1

    if 15 in usedBasis:
        fA104 = 4*cos(8*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA104*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB104 = 4*sin(8*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FB += SF.ai[idx_a]*fB104*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,4])
        idx_a += 1

    if 16 in usedBasis:
        fA311 = -2*cos(2*z*pi)*(cos(2*pi*(4*x - y)) + cos(2*pi*(3*x - 4*y)) - cos(2*pi*(4*x - 3*y)) + cos(2*pi*(x + 3*y)) - cos(2*pi*(3*x + y)) - cos(2*pi*(x - 4*y)))
        FA += SF.ai[idx_a]*fA311*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB311 = -2*sin(2*z*pi)*(cos(2*pi*(4*x - y)) + cos(2*pi*(3*x - 4*y)) - cos(2*pi*(4*x - 3*y)) + cos(2*pi*(x + 3*y)) - cos(2*pi*(3*x + y)) - cos(2*pi*(x - 4*y)))
        FB += SF.ai[idx_a]*fB311*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,1])
        idx_a += 1

    if 17 in usedBasis:
        fA213 = -2*cos(6*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) - cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) - cos(2*pi*(2*x + y)) - cos(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA213*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB213 = -2*sin(6*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) - cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) - cos(2*pi*(2*x + y)) - cos(2*pi*(x - 3*y)))
        FB += SF.ai[idx_a]*fB213*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,3])
        idx_a += 1

    if 18 in usedBasis:
        fA222 = 4*cos(4*z*pi)*(cos(4*pi*(2*x - y)) + cos(4*pi*(x + y)) + cos(4*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA222*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB222 = 4*sin(4*z*pi)*(cos(4*pi*(2*x - y)) + cos(4*pi*(x + y)) + cos(4*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB222*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,2])
        idx_a += 1

    if 19 in usedBasis:
        fA114 = 4*cos(8*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA114*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB114 = 4*sin(8*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB114*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,4])
        idx_a += 1

    if 20 in usedBasis:
        fA400 = 4*cos(8*x*pi) + 4*cos(8*y*pi) + 4*cos(8*pi*(x - y))
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 21 in usedBasis:
        fA312 = 2*cos(4*z*pi)*(cos(2*pi*(4*x - y)) + cos(2*pi*(3*x - 4*y)) + cos(2*pi*(4*x - 3*y)) + cos(2*pi*(x + 3*y)) + cos(2*pi*(3*x + y)) + cos(2*pi*(x - 4*y)))
        FA += SF.ai[idx_a]*fA312*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB312 = 2*sin(4*z*pi)*(cos(2*pi*(4*x - y)) + cos(2*pi*(3*x - 4*y)) + cos(2*pi*(4*x - 3*y)) + cos(2*pi*(x + 3*y)) + cos(2*pi*(3*x + y)) + cos(2*pi*(x - 4*y)))
        FB += SF.ai[idx_a]*fB312*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,2])
        idx_a += 1

    if 22 in usedBasis:
        fA204 = 4*cos(8*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA204*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB204 = 4*sin(8*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FB += SF.ai[idx_a]*fB204*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,4])
        idx_a += 1

    if 23 in usedBasis:
        fA320 = 2*cos(2*pi*(2*x + 3*y)) + 2*cos(2*pi*(3*x + 2*y)) + 2*cos(2*pi*(2*x - 5*y)) + 2*cos(2*pi*(5*x - 2*y)) + 2*cos(2*pi*(3*x - 5*y)) + 2*cos(2*pi*(5*x - 3*y))
        FA += SF.ai[idx_a]*fA320*Multi[idx_a]
        hkl.append([3,2,0])
        idx_a += 1

    if 24 in usedBasis:
        fA402 = 4*cos(4*z*pi)*(cos(8*x*pi) + cos(8*y*pi) + cos(8*pi*(x - y)))
        FA += SF.ai[idx_a]*fA402*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB402 = 4*sin(4*z*pi)*(cos(8*x*pi) + cos(8*y*pi) + cos(8*pi*(x - y)))
        FB += SF.ai[idx_a]*fB402*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,0,2])
        idx_a += 1

    if 25 in usedBasis:
        fA214 = 2*cos(8*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA214*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB214 = 2*sin(8*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FB += SF.ai[idx_a]*fB214*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,4])
        idx_a += 1

    if 26 in usedBasis:
        fA321 = -2*cos(2*z*pi)*(cos(2*pi*(2*x + 3*y)) - cos(2*pi*(3*x + 2*y)) - cos(2*pi*(2*x - 5*y)) + cos(2*pi*(5*x - 2*y)) + cos(2*pi*(3*x - 5*y)) - cos(2*pi*(5*x - 3*y)))
        FA += SF.ai[idx_a]*fA321*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB321 = -2*sin(2*z*pi)*(cos(2*pi*(2*x + 3*y)) - cos(2*pi*(3*x + 2*y)) - cos(2*pi*(2*x - 5*y)) + cos(2*pi*(5*x - 2*y)) + cos(2*pi*(3*x - 5*y)) - cos(2*pi*(5*x - 3*y)))
        FB += SF.ai[idx_a]*fB321*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,1])
        idx_a += 1

    if 27 in usedBasis:
        fA313 = -2*cos(6*z*pi)*(cos(2*pi*(4*x - y)) + cos(2*pi*(3*x - 4*y)) - cos(2*pi*(4*x - 3*y)) + cos(2*pi*(x + 3*y)) - cos(2*pi*(3*x + y)) - cos(2*pi*(x - 4*y)))
        FA += SF.ai[idx_a]*fA313*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB313 = -2*sin(6*z*pi)*(cos(2*pi*(4*x - y)) + cos(2*pi*(3*x - 4*y)) - cos(2*pi*(4*x - 3*y)) + cos(2*pi*(x + 3*y)) - cos(2*pi*(3*x + y)) - cos(2*pi*(x - 4*y)))
        FB += SF.ai[idx_a]*fB313*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,3])
        idx_a += 1

    if 28 in usedBasis:
        fA410 = 2*cos(2*pi*(5*x - y)) + 2*cos(2*pi*(4*x - 5*y)) + 2*cos(2*pi*(5*x - 4*y)) + 2*cos(2*pi*(x + 4*y)) + 2*cos(2*pi*(4*x + y)) + 2*cos(2*pi*(x - 5*y))
        FA += SF.ai[idx_a]*fA410*Multi[idx_a]
        hkl.append([4,1,0])
        idx_a += 1

    if 29 in usedBasis:
        fA304 = 4*cos(8*z*pi)*(cos(6*x*pi) + cos(6*y*pi) + cos(6*pi*(x - y)))
        FA += SF.ai[idx_a]*fA304*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB304 = 4*sin(8*z*pi)*(cos(6*x*pi) + cos(6*y*pi) + cos(6*pi*(x - y)))
        FB += SF.ai[idx_a]*fB304*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,4])
        idx_a += 1

    if 30 in usedBasis:
        fA411 = -2*cos(2*z*pi)*(cos(2*pi*(5*x - y)) + cos(2*pi*(4*x - 5*y)) - cos(2*pi*(5*x - 4*y)) + cos(2*pi*(x + 4*y)) - cos(2*pi*(4*x + y)) - cos(2*pi*(x - 5*y)))
        FA += SF.ai[idx_a]*fA411*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB411 = -2*sin(2*z*pi)*(cos(2*pi*(5*x - y)) + cos(2*pi*(4*x - 5*y)) - cos(2*pi*(5*x - 4*y)) + cos(2*pi*(x + 4*y)) - cos(2*pi*(4*x + y)) - cos(2*pi*(x - 5*y)))
        FB += SF.ai[idx_a]*fB411*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,1,1])
        idx_a += 1

    if 31 in usedBasis:
        fA322 = 2*cos(4*z*pi)*(cos(2*pi*(2*x + 3*y)) + cos(2*pi*(3*x + 2*y)) + cos(2*pi*(2*x - 5*y)) + cos(2*pi*(5*x - 2*y)) + cos(2*pi*(3*x - 5*y)) + cos(2*pi*(5*x - 3*y)))
        FA += SF.ai[idx_a]*fA322*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB322 = 2*sin(4*z*pi)*(cos(2*pi*(2*x + 3*y)) + cos(2*pi*(3*x + 2*y)) + cos(2*pi*(2*x - 5*y)) + cos(2*pi*(5*x - 2*y)) + cos(2*pi*(3*x - 5*y)) + cos(2*pi*(5*x - 3*y)))
        FB += SF.ai[idx_a]*fB322*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,2])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 1 0 1 1 0 1 1 0 1 0 1 1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 
    # 184: [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
    return FA+FB, idx_theta, hkl
