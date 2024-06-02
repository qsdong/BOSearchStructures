# Generated at 2024-02-23 17:37:18
# Qingshu Dong

import numpy as np

def  calF_193(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([6, 6, 2, 12, 6, 12, 12, 12, 12, 24, 6, 12, 24, 6, 12, 2, 12, 12, 12, 24, 24, 12, 12, 6, 24, 12, 12, 12, 12, 24, 24, 24])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 193.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA100 = 8*cos(2*x*pi) + 8*cos(2*y*pi) + 8*cos(2*pi*(x - y))
        FA += SF.ai[idx_a]*fA100*Multi[idx_a]
        hkl.append([1,0,0])
        idx_a += 1

    if 1 in usedBasis:
        fA110 = 8*cos(2*pi*(2*x - y)) + 8*cos(2*pi*(x + y)) + 8*cos(2*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 2 in usedBasis:
        fA002 = 24*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA002*Multi[idx_a]
        hkl.append([0,0,2])
        idx_a += 1

    if 3 in usedBasis:
        fA111 = -8*sin(2*z*pi)*(sin(2*pi*(x + y)) - sin(2*pi*(2*x - y)) + sin(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA111*Multi[idx_a]
        hkl.append([1,1,1])
        idx_a += 1

    if 4 in usedBasis:
        fA200 = 8*cos(4*x*pi) + 8*cos(4*y*pi) + 8*cos(4*pi*(x - y))
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 5 in usedBasis:
        fA102 = 8*cos(4*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA102*Multi[idx_a]
        hkl.append([1,0,2])
        idx_a += 1

    if 6 in usedBasis:
        fA112 = 8*cos(4*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA112*Multi[idx_a]
        hkl.append([1,1,2])
        idx_a += 1

    if 7 in usedBasis:
        fA210 = 4*cos(2*pi*(3*x - y)) + 4*cos(2*pi*(2*x - 3*y)) + 4*cos(2*pi*(3*x - 2*y)) + 4*cos(2*pi*(x + 2*y)) + 4*cos(2*pi*(2*x + y)) + 4*cos(2*pi*(x - 3*y))
        FA += SF.ai[idx_a]*fA210*Multi[idx_a]
        hkl.append([2,1,0])
        idx_a += 1

    if 8 in usedBasis:
        fA202 = 8*cos(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA202*Multi[idx_a]
        hkl.append([2,0,2])
        idx_a += 1

    if 9 in usedBasis:
        fA211 = -4*sin(2*z*pi)*(sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - y)) - sin(2*pi*(3*x - 2*y)) + sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA211*Multi[idx_a]
        hkl.append([2,1,1])
        idx_a += 1

    if 10 in usedBasis:
        fA300 = 8*cos(6*x*pi) + 8*cos(6*y*pi) + 8*cos(6*pi*(x - y))
        FA += SF.ai[idx_a]*fA300*Multi[idx_a]
        hkl.append([3,0,0])
        idx_a += 1

    if 11 in usedBasis:
        fA113 = -8*sin(6*z*pi)*(sin(2*pi*(x + y)) - sin(2*pi*(2*x - y)) + sin(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA113*Multi[idx_a]
        hkl.append([1,1,3])
        idx_a += 1

    if 12 in usedBasis:
        fA212 = 4*cos(4*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA212*Multi[idx_a]
        hkl.append([2,1,2])
        idx_a += 1

    if 13 in usedBasis:
        fA220 = 8*cos(4*pi*(2*x - y)) + 8*cos(4*pi*(x + y)) + 8*cos(4*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 14 in usedBasis:
        fA302 = 8*cos(4*z*pi)*(cos(6*x*pi) + cos(6*y*pi) + cos(6*pi*(x - y)))
        FA += SF.ai[idx_a]*fA302*Multi[idx_a]
        hkl.append([3,0,2])
        idx_a += 1

    if 15 in usedBasis:
        fA004 = 24*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA004*Multi[idx_a]
        hkl.append([0,0,4])
        idx_a += 1

    if 16 in usedBasis:
        fA221 = -8*sin(2*z*pi)*(sin(4*pi*(x + y)) - sin(4*pi*(2*x - y)) + sin(4*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA221*Multi[idx_a]
        hkl.append([2,2,1])
        idx_a += 1

    if 17 in usedBasis:
        fA310 = 4*cos(2*pi*(4*x - y)) + 4*cos(2*pi*(3*x - 4*y)) + 4*cos(2*pi*(4*x - 3*y)) + 4*cos(2*pi*(x + 3*y)) + 4*cos(2*pi*(3*x + y)) + 4*cos(2*pi*(x - 4*y))
        FA += SF.ai[idx_a]*fA310*Multi[idx_a]
        hkl.append([3,1,0])
        idx_a += 1

    if 18 in usedBasis:
        fA104 = 8*cos(8*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA104*Multi[idx_a]
        hkl.append([1,0,4])
        idx_a += 1

    if 19 in usedBasis:
        fA311 = -4*sin(2*z*pi)*(sin(2*pi*(3*x - 4*y)) - sin(2*pi*(4*x - y)) - sin(2*pi*(4*x - 3*y)) + sin(2*pi*(x + 3*y)) + sin(2*pi*(3*x + y)) + sin(2*pi*(x - 4*y)))
        FA += SF.ai[idx_a]*fA311*Multi[idx_a]
        hkl.append([3,1,1])
        idx_a += 1

    if 20 in usedBasis:
        fA213 = -4*sin(6*z*pi)*(sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - y)) - sin(2*pi*(3*x - 2*y)) + sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA213*Multi[idx_a]
        hkl.append([2,1,3])
        idx_a += 1

    if 21 in usedBasis:
        fA222 = 8*cos(4*z*pi)*(cos(4*pi*(2*x - y)) + cos(4*pi*(x + y)) + cos(4*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA222*Multi[idx_a]
        hkl.append([2,2,2])
        idx_a += 1

    if 22 in usedBasis:
        fA114 = 8*cos(8*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA114*Multi[idx_a]
        hkl.append([1,1,4])
        idx_a += 1

    if 23 in usedBasis:
        fA400 = 8*cos(8*x*pi) + 8*cos(8*y*pi) + 8*cos(8*pi*(x - y))
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 24 in usedBasis:
        fA312 = 4*cos(4*z*pi)*(cos(2*pi*(4*x - y)) + cos(2*pi*(3*x - 4*y)) + cos(2*pi*(4*x - 3*y)) + cos(2*pi*(x + 3*y)) + cos(2*pi*(3*x + y)) + cos(2*pi*(x - 4*y)))
        FA += SF.ai[idx_a]*fA312*Multi[idx_a]
        hkl.append([3,1,2])
        idx_a += 1

    if 25 in usedBasis:
        fA204 = 8*cos(8*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA204*Multi[idx_a]
        hkl.append([2,0,4])
        idx_a += 1

    if 26 in usedBasis:
        fA223 = -8*sin(6*z*pi)*(sin(4*pi*(x + y)) - sin(4*pi*(2*x - y)) + sin(4*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA223*Multi[idx_a]
        hkl.append([2,2,3])
        idx_a += 1

    if 27 in usedBasis:
        fA320 = 4*cos(2*pi*(2*x + 3*y)) + 4*cos(2*pi*(3*x + 2*y)) + 4*cos(2*pi*(2*x - 5*y)) + 4*cos(2*pi*(5*x - 2*y)) + 4*cos(2*pi*(3*x - 5*y)) + 4*cos(2*pi*(5*x - 3*y))
        FA += SF.ai[idx_a]*fA320*Multi[idx_a]
        hkl.append([3,2,0])
        idx_a += 1

    if 28 in usedBasis:
        fA402 = 8*cos(4*z*pi)*(cos(8*x*pi) + cos(8*y*pi) + cos(8*pi*(x - y)))
        FA += SF.ai[idx_a]*fA402*Multi[idx_a]
        hkl.append([4,0,2])
        idx_a += 1

    if 29 in usedBasis:
        fA214 = 4*cos(8*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA214*Multi[idx_a]
        hkl.append([2,1,4])
        idx_a += 1

    if 30 in usedBasis:
        fA321 = -4*sin(2*z*pi)*(sin(2*pi*(2*x + 3*y)) + sin(2*pi*(3*x + 2*y)) + sin(2*pi*(2*x - 5*y)) - sin(2*pi*(5*x - 2*y)) + sin(2*pi*(3*x - 5*y)) - sin(2*pi*(5*x - 3*y)))
        FA += SF.ai[idx_a]*fA321*Multi[idx_a]
        hkl.append([3,2,1])
        idx_a += 1

    if 31 in usedBasis:
        fA313 = -4*sin(6*z*pi)*(sin(2*pi*(3*x - 4*y)) - sin(2*pi*(4*x - y)) - sin(2*pi*(4*x - 3*y)) + sin(2*pi*(x + 3*y)) + sin(2*pi*(3*x + y)) + sin(2*pi*(x - 4*y)))
        FA += SF.ai[idx_a]*fA313*Multi[idx_a]
        hkl.append([3,1,3])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    # 193: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return FA+FB, idx_theta, hkl
