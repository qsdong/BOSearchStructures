# Generated at 2023-12-02 18:58:07
# Qingshu Dong

import numpy as np

def  calF_310(SF,startBasis=0):
    [x,y] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([4, 4, 4, 8, 4, 4, 8, 8, 4, 8, 4, 8, 8, 4, 8, 8, 4, 8, 4, 8, 8, 8, 8, 4, 4, 8, 8, 8, 8, 8, 4, 8])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hk = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 10.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA10 = 2*cos(2*x*pi) + 2*cos(2*y*pi)
        FA += SF.ai[idx_a]*fA10*Multi[idx_a]
        hk.append([1,0])
        idx_a += 1

    if 1 in usedBasis:
        fA11 = 4*cos(2*x*pi)*cos(2*y*pi)
        FA += SF.ai[idx_a]*fA11*Multi[idx_a]
        hk.append([1,1])
        idx_a += 1

    if 2 in usedBasis:
        fA20 = 2*cos(4*x*pi) + 2*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA20*Multi[idx_a]
        hk.append([2,0])
        idx_a += 1

    if 3 in usedBasis:
        fA21 = 2*cos(2*pi*(x - 2*y)) + 2*cos(2*pi*(2*x + y))
        FA += SF.ai[idx_a]*fA21*Multi[idx_a]
        hk.append([2,1])
        idx_a += 1

    if 4 in usedBasis:
        fA22 = 4*cos(4*x*pi)*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA22*Multi[idx_a]
        hk.append([2,2])
        idx_a += 1

    if 5 in usedBasis:
        fA30 = 2*cos(6*x*pi) + 2*cos(6*y*pi)
        FA += SF.ai[idx_a]*fA30*Multi[idx_a]
        hk.append([3,0])
        idx_a += 1

    if 6 in usedBasis:
        fA31 = 2*cos(2*pi*(x - 3*y)) + 2*cos(2*pi*(3*x + y))
        FA += SF.ai[idx_a]*fA31*Multi[idx_a]
        hk.append([3,1])
        idx_a += 1

    if 7 in usedBasis:
        fA32 = 2*cos(2*pi*(2*x - 3*y)) + 2*cos(2*pi*(3*x + 2*y))
        FA += SF.ai[idx_a]*fA32*Multi[idx_a]
        hk.append([3,2])
        idx_a += 1

    if 8 in usedBasis:
        fA40 = 2*cos(8*x*pi) + 2*cos(8*y*pi)
        FA += SF.ai[idx_a]*fA40*Multi[idx_a]
        hk.append([4,0])
        idx_a += 1

    if 9 in usedBasis:
        fA41 = 2*cos(2*pi*(x - 4*y)) + 2*cos(2*pi*(4*x + y))
        FA += SF.ai[idx_a]*fA41*Multi[idx_a]
        hk.append([4,1])
        idx_a += 1

    if 10 in usedBasis:
        fA33 = 4*cos(6*x*pi)*cos(6*y*pi)
        FA += SF.ai[idx_a]*fA33*Multi[idx_a]
        hk.append([3,3])
        idx_a += 1

    if 11 in usedBasis:
        fA42 = 2*cos(4*pi*(x - 2*y)) + 2*cos(4*pi*(2*x + y))
        FA += SF.ai[idx_a]*fA42*Multi[idx_a]
        hk.append([4,2])
        idx_a += 1

    if 12 in usedBasis:
        fA43 = 2*cos(2*pi*(3*x - 4*y)) + 2*cos(2*pi*(4*x + 3*y))
        FA += SF.ai[idx_a]*fA43*Multi[idx_a]
        hk.append([4,3])
        idx_a += 1

    if 13 in usedBasis:
        fA50 = 2*cos(10*x*pi) + 2*cos(10*y*pi)
        FA += SF.ai[idx_a]*fA50*Multi[idx_a]
        hk.append([5,0])
        idx_a += 1

    if 14 in usedBasis:
        fA51 = 2*cos(2*pi*(x - 5*y)) + 2*cos(2*pi*(5*x + y))
        FA += SF.ai[idx_a]*fA51*Multi[idx_a]
        hk.append([5,1])
        idx_a += 1

    if 15 in usedBasis:
        fA52 = 2*cos(2*pi*(2*x - 5*y)) + 2*cos(2*pi*(5*x + 2*y))
        FA += SF.ai[idx_a]*fA52*Multi[idx_a]
        hk.append([5,2])
        idx_a += 1

    if 16 in usedBasis:
        fA44 = 4*cos(8*x*pi)*cos(8*y*pi)
        FA += SF.ai[idx_a]*fA44*Multi[idx_a]
        hk.append([4,4])
        idx_a += 1

    if 17 in usedBasis:
        fA53 = 2*cos(2*pi*(3*x - 5*y)) + 2*cos(2*pi*(5*x + 3*y))
        FA += SF.ai[idx_a]*fA53*Multi[idx_a]
        hk.append([5,3])
        idx_a += 1

    if 18 in usedBasis:
        fA60 = 2*cos(12*x*pi) + 2*cos(12*y*pi)
        FA += SF.ai[idx_a]*fA60*Multi[idx_a]
        hk.append([6,0])
        idx_a += 1

    if 19 in usedBasis:
        fA61 = 2*cos(2*pi*(x - 6*y)) + 2*cos(2*pi*(6*x + y))
        FA += SF.ai[idx_a]*fA61*Multi[idx_a]
        hk.append([6,1])
        idx_a += 1

    if 20 in usedBasis:
        fA62 = 2*cos(4*pi*(x - 3*y)) + 2*cos(4*pi*(3*x + y))
        FA += SF.ai[idx_a]*fA62*Multi[idx_a]
        hk.append([6,2])
        idx_a += 1

    if 21 in usedBasis:
        fA54 = 2*cos(2*pi*(4*x - 5*y)) + 2*cos(2*pi*(5*x + 4*y))
        FA += SF.ai[idx_a]*fA54*Multi[idx_a]
        hk.append([5,4])
        idx_a += 1

    if 22 in usedBasis:
        fA63 = 2*cos(6*pi*(x - 2*y)) + 2*cos(6*pi*(2*x + y))
        FA += SF.ai[idx_a]*fA63*Multi[idx_a]
        hk.append([6,3])
        idx_a += 1

    if 23 in usedBasis:
        fA70 = 2*cos(14*x*pi) + 2*cos(14*y*pi)
        FA += SF.ai[idx_a]*fA70*Multi[idx_a]
        hk.append([7,0])
        idx_a += 1

    if 24 in usedBasis:
        fA55 = 4*cos(10*x*pi)*cos(10*y*pi)
        FA += SF.ai[idx_a]*fA55*Multi[idx_a]
        hk.append([5,5])
        idx_a += 1

    if 25 in usedBasis:
        fA71 = 2*cos(2*pi*(x - 7*y)) + 2*cos(2*pi*(7*x + y))
        FA += SF.ai[idx_a]*fA71*Multi[idx_a]
        hk.append([7,1])
        idx_a += 1

    if 26 in usedBasis:
        fA64 = 2*cos(4*pi*(2*x - 3*y)) + 2*cos(4*pi*(3*x + 2*y))
        FA += SF.ai[idx_a]*fA64*Multi[idx_a]
        hk.append([6,4])
        idx_a += 1

    if 27 in usedBasis:
        fA72 = 2*cos(2*pi*(2*x - 7*y)) + 2*cos(2*pi*(7*x + 2*y))
        FA += SF.ai[idx_a]*fA72*Multi[idx_a]
        hk.append([7,2])
        idx_a += 1

    if 28 in usedBasis:
        fA73 = 2*cos(2*pi*(3*x - 7*y)) + 2*cos(2*pi*(7*x + 3*y))
        FA += SF.ai[idx_a]*fA73*Multi[idx_a]
        hk.append([7,3])
        idx_a += 1

    if 29 in usedBasis:
        fA65 = 2*cos(2*pi*(5*x - 6*y)) + 2*cos(2*pi*(6*x + 5*y))
        FA += SF.ai[idx_a]*fA65*Multi[idx_a]
        hk.append([6,5])
        idx_a += 1

    if 30 in usedBasis:
        fA80 = 2*cos(16*x*pi) + 2*cos(16*y*pi)
        FA += SF.ai[idx_a]*fA80*Multi[idx_a]
        hk.append([8,0])
        idx_a += 1

    if 31 in usedBasis:
        fA74 = 2*cos(2*pi*(4*x - 7*y)) + 2*cos(2*pi*(7*x + 4*y))
        FA += SF.ai[idx_a]*fA74*Multi[idx_a]
        hk.append([7,4])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    # 310: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return FA+FB, idx_theta, hk
