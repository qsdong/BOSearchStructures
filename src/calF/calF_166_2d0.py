# Generated at 2024-03-12 09:19:50
# Qingshu Dong

import numpy as np

def  calF_166_2d0(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([12, 2, 6, 12, 12, 12, 2, 24, 12, 6, 12, 24, 12, 12, 6, 12, 24, 2, 12, 12, 12, 24, 24, 12, 12, 12, 24, 12, 12, 24, 24, 12])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 166.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA101 = 12*cos(2*pi*(y - x + z)) + 12*cos(2*pi*(x + z)) + 12*cos(2*pi*(y - z))
        FA += SF.ai[idx_a]*fA101*Multi[idx_a]
        hkl.append([1,0,1])
        idx_a += 1

    if 1 in usedBasis:
        fA003 = 36*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA003*Multi[idx_a]
        hkl.append([0,0,3])
        idx_a += 1

    if 2 in usedBasis:
        fA110 = 12*cos(2*pi*(2*x - y)) + 12*cos(2*pi*(x + y)) + 12*cos(2*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 3 in usedBasis:
        fA104 = 12*cos(2*pi*(y - x + 4*z)) + 12*cos(2*pi*(x + 4*z)) + 12*cos(2*pi*(y - 4*z))
        FA += SF.ai[idx_a]*fA104*Multi[idx_a]
        hkl.append([1,0,4])
        idx_a += 1

    if 4 in usedBasis:
        fA113 = 12*cos(6*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA113*Multi[idx_a]
        hkl.append([1,1,3])
        idx_a += 1

    if 5 in usedBasis:
        fA202 = 12*cos(4*pi*(y - x + z)) + 12*cos(4*pi*(x + z)) + 12*cos(4*pi*(y - z))
        FA += SF.ai[idx_a]*fA202*Multi[idx_a]
        hkl.append([2,0,2])
        idx_a += 1

    if 6 in usedBasis:
        fA006 = 36*cos(12*z*pi)
        FA += SF.ai[idx_a]*fA006*Multi[idx_a]
        hkl.append([0,0,6])
        idx_a += 1

    if 7 in usedBasis:
        fA211 = 6*cos(2*pi*(2*x + y + z)) + 6*cos(2*pi*(x - 3*y + z)) + 6*cos(2*pi*(x + 2*y - z)) + 6*cos(2*pi*(3*x - y + z)) + 6*cos(2*pi*(3*y - 2*x + z)) + 6*cos(2*pi*(2*y - 3*x + z))
        FA += SF.ai[idx_a]*fA211*Multi[idx_a]
        hkl.append([2,1,1])
        idx_a += 1

    if 8 in usedBasis:
        fA205 = 12*cos(2*pi*(2*x + 5*z)) + 12*cos(2*pi*(2*y - 5*z)) + 12*cos(2*pi*(2*y - 2*x + 5*z))
        FA += SF.ai[idx_a]*fA205*Multi[idx_a]
        hkl.append([2,0,5])
        idx_a += 1

    if 9 in usedBasis:
        fA300 = 12*cos(6*x*pi) + 12*cos(6*y*pi) + 12*cos(6*pi*(x - y))
        FA += SF.ai[idx_a]*fA300*Multi[idx_a]
        hkl.append([3,0,0])
        idx_a += 1

    if 10 in usedBasis:
        fA116 = 12*cos(12*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA116*Multi[idx_a]
        hkl.append([1,1,6])
        idx_a += 1

    if 11 in usedBasis:
        fA214 = 6*cos(2*pi*(x + 2*y - 4*z)) + 6*cos(2*pi*(2*x + y + 4*z)) + 6*cos(2*pi*(x - 3*y + 4*z)) + 6*cos(2*pi*(3*x - y + 4*z)) + 6*cos(2*pi*(3*y - 2*x + 4*z)) + 6*cos(2*pi*(2*y - 3*x + 4*z))
        FA += SF.ai[idx_a]*fA214*Multi[idx_a]
        hkl.append([2,1,4])
        idx_a += 1

    if 12 in usedBasis:
        fA107 = 12*cos(2*pi*(y - x + 7*z)) + 12*cos(2*pi*(x + 7*z)) + 12*cos(2*pi*(y - 7*z))
        FA += SF.ai[idx_a]*fA107*Multi[idx_a]
        hkl.append([1,0,7])
        idx_a += 1

    if 13 in usedBasis:
        fA303 = 12*cos(6*pi*(y - x + z)) + 12*cos(6*pi*(x + z)) + 12*cos(6*pi*(y - z))
        FA += SF.ai[idx_a]*fA303*Multi[idx_a]
        hkl.append([3,0,3])
        idx_a += 1

    if 14 in usedBasis:
        fA220 = 12*cos(4*pi*(2*x - y)) + 12*cos(4*pi*(x + y)) + 12*cos(4*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 15 in usedBasis:
        fA223 = 12*cos(6*z*pi)*(cos(4*pi*(2*x - y)) + cos(4*pi*(x + y)) + cos(4*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA223*Multi[idx_a]
        hkl.append([2,2,3])
        idx_a += 1

    if 16 in usedBasis:
        fA312 = 6*cos(2*pi*(x + 3*y - 2*z)) + 6*cos(2*pi*(3*x + y + 2*z)) + 6*cos(2*pi*(x - 4*y + 2*z)) + 6*cos(2*pi*(4*x - y + 2*z)) + 6*cos(2*pi*(4*y - 3*x + 2*z)) + 6*cos(2*pi*(3*y - 4*x + 2*z))
        FA += SF.ai[idx_a]*fA312*Multi[idx_a]
        hkl.append([3,1,2])
        idx_a += 1

    if 17 in usedBasis:
        fA009 = 36*cos(18*z*pi)
        FA += SF.ai[idx_a]*fA009*Multi[idx_a]
        hkl.append([0,0,9])
        idx_a += 1

    if 18 in usedBasis:
        fA306 = 12*cos(6*pi*(y - x + 2*z)) + 12*cos(6*pi*(x + 2*z)) + 12*cos(6*pi*(y - 2*z))
        FA += SF.ai[idx_a]*fA306*Multi[idx_a]
        hkl.append([3,0,6])
        idx_a += 1

    if 19 in usedBasis:
        fA208 = 12*cos(4*pi*(y - x + 4*z)) + 12*cos(4*pi*(x + 4*z)) + 12*cos(4*pi*(y - 4*z))
        FA += SF.ai[idx_a]*fA208*Multi[idx_a]
        hkl.append([2,0,8])
        idx_a += 1

    if 20 in usedBasis:
        fA401 = 12*cos(2*pi*(4*y - z)) + 12*cos(2*pi*(4*y - 4*x + z)) + 12*cos(2*pi*(4*x + z))
        FA += SF.ai[idx_a]*fA401*Multi[idx_a]
        hkl.append([4,0,1])
        idx_a += 1

    if 21 in usedBasis:
        fA217 = 6*cos(2*pi*(x + 2*y - 7*z)) + 6*cos(2*pi*(2*x + y + 7*z)) + 6*cos(2*pi*(x - 3*y + 7*z)) + 6*cos(2*pi*(3*x - y + 7*z)) + 6*cos(2*pi*(3*y - 2*x + 7*z)) + 6*cos(2*pi*(2*y - 3*x + 7*z))
        FA += SF.ai[idx_a]*fA217*Multi[idx_a]
        hkl.append([2,1,7])
        idx_a += 1

    if 22 in usedBasis:
        fA315 = 6*cos(2*pi*(x + 3*y - 5*z)) + 6*cos(2*pi*(3*x + y + 5*z)) + 6*cos(2*pi*(x - 4*y + 5*z)) + 6*cos(2*pi*(4*x - y + 5*z)) + 6*cos(2*pi*(4*y - 3*x + 5*z)) + 6*cos(2*pi*(3*y - 4*x + 5*z))
        FA += SF.ai[idx_a]*fA315*Multi[idx_a]
        hkl.append([3,1,5])
        idx_a += 1

    if 23 in usedBasis:
        fA119 = 12*cos(18*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA119*Multi[idx_a]
        hkl.append([1,1,9])
        idx_a += 1

    if 24 in usedBasis:
        fA226 = 12*cos(12*z*pi)*(cos(4*pi*(2*x - y)) + cos(4*pi*(x + y)) + cos(4*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA226*Multi[idx_a]
        hkl.append([2,2,6])
        idx_a += 1

    if 25 in usedBasis:
        fA404 = 12*cos(8*pi*(y - x + z)) + 12*cos(8*pi*(x + z)) + 12*cos(8*pi*(y - z))
        FA += SF.ai[idx_a]*fA404*Multi[idx_a]
        hkl.append([4,0,4])
        idx_a += 1

    if 26 in usedBasis:
        fA321 = 6*cos(2*pi*(3*x + 2*y + z)) + 6*cos(2*pi*(2*x - 5*y + z)) + 6*cos(2*pi*(5*x - 2*y + z)) + 6*cos(2*pi*(5*y - 3*x + z)) + 6*cos(2*pi*(3*y - 5*x + z)) + 6*cos(2*pi*(2*x + 3*y - z))
        FA += SF.ai[idx_a]*fA321*Multi[idx_a]
        hkl.append([3,2,1])
        idx_a += 1

    if 27 in usedBasis:
        fA1010 = 12*cos(2*pi*(y - x + 10*z)) + 12*cos(2*pi*(x + 10*z)) + 12*cos(2*pi*(y - 10*z))
        FA += SF.ai[idx_a]*fA1010*Multi[idx_a]
        hkl.append([1,0,10])
        idx_a += 1

    if 28 in usedBasis:
        fA410 = 6*cos(2*pi*(5*x - y)) + 6*cos(2*pi*(4*x - 5*y)) + 6*cos(2*pi*(5*x - 4*y)) + 6*cos(2*pi*(x + 4*y)) + 6*cos(2*pi*(4*x + y)) + 6*cos(2*pi*(x - 5*y))
        FA += SF.ai[idx_a]*fA410*Multi[idx_a]
        hkl.append([4,1,0])
        idx_a += 1

    if 29 in usedBasis:
        fA324 = 6*cos(2*pi*(2*x + 3*y - 4*z)) + 6*cos(2*pi*(3*x + 2*y + 4*z)) + 6*cos(2*pi*(2*x - 5*y + 4*z)) + 6*cos(2*pi*(5*x - 2*y + 4*z)) + 6*cos(2*pi*(5*y - 3*x + 4*z)) + 6*cos(2*pi*(3*y - 5*x + 4*z))
        FA += SF.ai[idx_a]*fA324*Multi[idx_a]
        hkl.append([3,2,4])
        idx_a += 1

    if 30 in usedBasis:
        fA413 = 6*cos(2*pi*(x + 4*y - 3*z)) + 6*cos(2*pi*(4*x + y + 3*z)) + 6*cos(2*pi*(x - 5*y + 3*z)) + 6*cos(2*pi*(5*x - y + 3*z)) + 6*cos(2*pi*(5*y - 4*x + 3*z)) + 6*cos(2*pi*(4*y - 5*x + 3*z))
        FA += SF.ai[idx_a]*fA413*Multi[idx_a]
        hkl.append([4,1,3])
        idx_a += 1

    if 31 in usedBasis:
        fA309 = 12*cos(6*pi*(y - x + 3*z)) + 12*cos(6*pi*(x + 3*z)) + 12*cos(6*pi*(y - 3*z))
        FA += SF.ai[idx_a]*fA309*Multi[idx_a]
        hkl.append([3,0,9])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    # 166_2d0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return FA+FB, idx_theta, hkl
