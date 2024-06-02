# Generated at 2023-12-02 18:58:48
# Qingshu Dong

import numpy as np

def  calF_314(SF,startBasis=0):
    [x,y] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([6, 6, 6, 12, 6, 6, 12, 6, 12, 12, 6, 6, 12, 12, 6, 12, 12, 12, 6, 6, 12, 12, 12, 12, 12, 6, 12, 12, 6, 12, 12, 6])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hk = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 14.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA10 = 2*cos(2*x*pi) + 2*cos(2*y*pi) + 2*cos(2*pi*(x - y))
        FA += SF.ai[idx_a]*fA10*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB10 = 2*sin(2*x*pi) - 2*sin(2*y*pi) - 2*sin(2*pi*(x - y))
        FB += SF.ai[idx_a]*fB10*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([1,0])
        idx_a += 1

    if 1 in usedBasis:
        fA11 = 2*cos(2*pi*(2*x - y)) + 2*cos(2*pi*(x + y)) + 2*cos(2*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA11*Multi[idx_a]
        hk.append([1,1])
        idx_a += 1

    if 2 in usedBasis:
        fA20 = 2*cos(4*x*pi) + 2*cos(4*y*pi) + 2*cos(4*pi*(x - y))
        FA += SF.ai[idx_a]*fA20*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB20 = 2*sin(4*x*pi) - 2*sin(4*y*pi) - 2*sin(4*pi*(x - y))
        FB += SF.ai[idx_a]*fB20*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([2,0])
        idx_a += 1

    if 3 in usedBasis:
        fA21 = cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y))
        FA += SF.ai[idx_a]*fA21*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB21 = sin(2*pi*(3*x - y)) - sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - 2*y)) - sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y))
        FB += SF.ai[idx_a]*fB21*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([2,1])
        idx_a += 1

    if 4 in usedBasis:
        fA30 = 2*cos(6*x*pi) + 2*cos(6*y*pi) + 2*cos(6*pi*(x - y))
        FA += SF.ai[idx_a]*fA30*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB30 = 2*sin(6*x*pi) - 2*sin(6*y*pi) - 2*sin(6*pi*(x - y))
        FB += SF.ai[idx_a]*fB30*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([3,0])
        idx_a += 1

    if 5 in usedBasis:
        fA22 = 2*cos(4*pi*(2*x - y)) + 2*cos(4*pi*(x + y)) + 2*cos(4*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA22*Multi[idx_a]
        hk.append([2,2])
        idx_a += 1

    if 6 in usedBasis:
        fA31 = cos(2*pi*(4*x - y)) + cos(2*pi*(3*x - 4*y)) + cos(2*pi*(4*x - 3*y)) + cos(2*pi*(x + 3*y)) + cos(2*pi*(3*x + y)) + cos(2*pi*(x - 4*y))
        FA += SF.ai[idx_a]*fA31*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB31 = sin(2*pi*(4*x - y)) - sin(2*pi*(3*x - 4*y)) - sin(2*pi*(4*x - 3*y)) - sin(2*pi*(x + 3*y)) + sin(2*pi*(3*x + y)) + sin(2*pi*(x - 4*y))
        FB += SF.ai[idx_a]*fB31*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([3,1])
        idx_a += 1

    if 7 in usedBasis:
        fA40 = 2*cos(8*x*pi) + 2*cos(8*y*pi) + 2*cos(8*pi*(x - y))
        FA += SF.ai[idx_a]*fA40*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB40 = 2*sin(8*x*pi) - 2*sin(8*y*pi) - 2*sin(8*pi*(x - y))
        FB += SF.ai[idx_a]*fB40*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([4,0])
        idx_a += 1

    if 8 in usedBasis:
        fA32 = cos(2*pi*(2*x + 3*y)) + cos(2*pi*(3*x + 2*y)) + cos(2*pi*(2*x - 5*y)) + cos(2*pi*(5*x - 2*y)) + cos(2*pi*(3*x - 5*y)) + cos(2*pi*(5*x - 3*y))
        FA += SF.ai[idx_a]*fA32*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB32 = sin(2*pi*(3*x + 2*y)) - sin(2*pi*(2*x + 3*y)) + sin(2*pi*(2*x - 5*y)) + sin(2*pi*(5*x - 2*y)) - sin(2*pi*(3*x - 5*y)) - sin(2*pi*(5*x - 3*y))
        FB += SF.ai[idx_a]*fB32*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([3,2])
        idx_a += 1

    if 9 in usedBasis:
        fA41 = cos(2*pi*(5*x - y)) + cos(2*pi*(4*x - 5*y)) + cos(2*pi*(5*x - 4*y)) + cos(2*pi*(x + 4*y)) + cos(2*pi*(4*x + y)) + cos(2*pi*(x - 5*y))
        FA += SF.ai[idx_a]*fA41*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB41 = sin(2*pi*(5*x - y)) - sin(2*pi*(4*x - 5*y)) - sin(2*pi*(5*x - 4*y)) - sin(2*pi*(x + 4*y)) + sin(2*pi*(4*x + y)) + sin(2*pi*(x - 5*y))
        FB += SF.ai[idx_a]*fB41*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([4,1])
        idx_a += 1

    if 10 in usedBasis:
        fA50 = 2*cos(10*x*pi) + 2*cos(10*y*pi) + 2*cos(10*pi*(x - y))
        FA += SF.ai[idx_a]*fA50*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB50 = 2*sin(10*x*pi) - 2*sin(10*y*pi) - 2*sin(10*pi*(x - y))
        FB += SF.ai[idx_a]*fB50*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([5,0])
        idx_a += 1

    if 11 in usedBasis:
        fA33 = 2*cos(6*pi*(2*x - y)) + 2*cos(6*pi*(x + y)) + 2*cos(6*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA33*Multi[idx_a]
        hk.append([3,3])
        idx_a += 1

    if 12 in usedBasis:
        fA42 = cos(4*pi*(3*x - y)) + cos(4*pi*(2*x - 3*y)) + cos(4*pi*(3*x - 2*y)) + cos(4*pi*(x + 2*y)) + cos(4*pi*(2*x + y)) + cos(4*pi*(x - 3*y))
        FA += SF.ai[idx_a]*fA42*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB42 = sin(4*pi*(3*x - y)) - sin(4*pi*(2*x - 3*y)) - sin(4*pi*(3*x - 2*y)) - sin(4*pi*(x + 2*y)) + sin(4*pi*(2*x + y)) + sin(4*pi*(x - 3*y))
        FB += SF.ai[idx_a]*fB42*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([4,2])
        idx_a += 1

    if 13 in usedBasis:
        fA51 = cos(2*pi*(6*x - y)) + cos(2*pi*(5*x - 6*y)) + cos(2*pi*(6*x - 5*y)) + cos(2*pi*(x + 5*y)) + cos(2*pi*(5*x + y)) + cos(2*pi*(x - 6*y))
        FA += SF.ai[idx_a]*fA51*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB51 = sin(2*pi*(6*x - y)) - sin(2*pi*(5*x - 6*y)) - sin(2*pi*(6*x - 5*y)) - sin(2*pi*(x + 5*y)) + sin(2*pi*(5*x + y)) + sin(2*pi*(x - 6*y))
        FB += SF.ai[idx_a]*fB51*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([5,1])
        idx_a += 1

    if 14 in usedBasis:
        fA60 = 2*cos(12*x*pi) + 2*cos(12*y*pi) + 2*cos(12*pi*(x - y))
        FA += SF.ai[idx_a]*fA60*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB60 = 2*sin(12*x*pi) - 2*sin(12*y*pi) - 2*sin(12*pi*(x - y))
        FB += SF.ai[idx_a]*fB60*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([6,0])
        idx_a += 1

    if 15 in usedBasis:
        fA43 = cos(2*pi*(3*x + 4*y)) + cos(2*pi*(4*x + 3*y)) + cos(2*pi*(3*x - 7*y)) + cos(2*pi*(7*x - 3*y)) + cos(2*pi*(4*x - 7*y)) + cos(2*pi*(7*x - 4*y))
        FA += SF.ai[idx_a]*fA43*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB43 = sin(2*pi*(4*x + 3*y)) - sin(2*pi*(3*x + 4*y)) + sin(2*pi*(3*x - 7*y)) + sin(2*pi*(7*x - 3*y)) - sin(2*pi*(4*x - 7*y)) - sin(2*pi*(7*x - 4*y))
        FB += SF.ai[idx_a]*fB43*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([4,3])
        idx_a += 1

    if 16 in usedBasis:
        fA52 = cos(2*pi*(2*x + 5*y)) + cos(2*pi*(5*x + 2*y)) + cos(2*pi*(2*x - 7*y)) + cos(2*pi*(7*x - 2*y)) + cos(2*pi*(5*x - 7*y)) + cos(2*pi*(7*x - 5*y))
        FA += SF.ai[idx_a]*fA52*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB52 = sin(2*pi*(5*x + 2*y)) - sin(2*pi*(2*x + 5*y)) + sin(2*pi*(2*x - 7*y)) + sin(2*pi*(7*x - 2*y)) - sin(2*pi*(5*x - 7*y)) - sin(2*pi*(7*x - 5*y))
        FB += SF.ai[idx_a]*fB52*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([5,2])
        idx_a += 1

    if 17 in usedBasis:
        fA61 = cos(2*pi*(7*x - y)) + cos(2*pi*(6*x - 7*y)) + cos(2*pi*(7*x - 6*y)) + cos(2*pi*(x + 6*y)) + cos(2*pi*(6*x + y)) + cos(2*pi*(x - 7*y))
        FA += SF.ai[idx_a]*fA61*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB61 = sin(2*pi*(7*x - y)) - sin(2*pi*(6*x - 7*y)) - sin(2*pi*(7*x - 6*y)) - sin(2*pi*(x + 6*y)) + sin(2*pi*(6*x + y)) + sin(2*pi*(x - 7*y))
        FB += SF.ai[idx_a]*fB61*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([6,1])
        idx_a += 1

    if 18 in usedBasis:
        fA44 = 2*cos(8*pi*(2*x - y)) + 2*cos(8*pi*(x + y)) + 2*cos(8*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA44*Multi[idx_a]
        hk.append([4,4])
        idx_a += 1

    if 19 in usedBasis:
        fA70 = 2*cos(14*x*pi) + 2*cos(14*y*pi) + 2*cos(14*pi*(x - y))
        FA += SF.ai[idx_a]*fA70*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB70 = 2*sin(14*x*pi) - 2*sin(14*y*pi) - 2*sin(14*pi*(x - y))
        FB += SF.ai[idx_a]*fB70*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([7,0])
        idx_a += 1

    if 20 in usedBasis:
        fA53 = cos(2*pi*(3*x + 5*y)) + cos(2*pi*(5*x + 3*y)) + cos(2*pi*(3*x - 8*y)) + cos(2*pi*(8*x - 3*y)) + cos(2*pi*(5*x - 8*y)) + cos(2*pi*(8*x - 5*y))
        FA += SF.ai[idx_a]*fA53*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB53 = sin(2*pi*(5*x + 3*y)) - sin(2*pi*(3*x + 5*y)) + sin(2*pi*(3*x - 8*y)) + sin(2*pi*(8*x - 3*y)) - sin(2*pi*(5*x - 8*y)) - sin(2*pi*(8*x - 5*y))
        FB += SF.ai[idx_a]*fB53*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([5,3])
        idx_a += 1

    if 21 in usedBasis:
        fA62 = cos(4*pi*(4*x - y)) + cos(4*pi*(3*x - 4*y)) + cos(4*pi*(4*x - 3*y)) + cos(4*pi*(x + 3*y)) + cos(4*pi*(3*x + y)) + cos(4*pi*(x - 4*y))
        FA += SF.ai[idx_a]*fA62*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB62 = sin(4*pi*(4*x - y)) - sin(4*pi*(3*x - 4*y)) - sin(4*pi*(4*x - 3*y)) - sin(4*pi*(x + 3*y)) + sin(4*pi*(3*x + y)) + sin(4*pi*(x - 4*y))
        FB += SF.ai[idx_a]*fB62*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([6,2])
        idx_a += 1

    if 22 in usedBasis:
        fA71 = cos(2*pi*(8*x - y)) + cos(2*pi*(7*x - 8*y)) + cos(2*pi*(8*x - 7*y)) + cos(2*pi*(x + 7*y)) + cos(2*pi*(7*x + y)) + cos(2*pi*(x - 8*y))
        FA += SF.ai[idx_a]*fA71*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB71 = sin(2*pi*(8*x - y)) - sin(2*pi*(7*x - 8*y)) - sin(2*pi*(8*x - 7*y)) - sin(2*pi*(x + 7*y)) + sin(2*pi*(7*x + y)) + sin(2*pi*(x - 8*y))
        FB += SF.ai[idx_a]*fB71*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([7,1])
        idx_a += 1

    if 23 in usedBasis:
        fA54 = cos(2*pi*(4*x + 5*y)) + cos(2*pi*(5*x + 4*y)) + cos(2*pi*(4*x - 9*y)) + cos(2*pi*(9*x - 4*y)) + cos(2*pi*(5*x - 9*y)) + cos(2*pi*(9*x - 5*y))
        FA += SF.ai[idx_a]*fA54*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB54 = sin(2*pi*(5*x + 4*y)) - sin(2*pi*(4*x + 5*y)) + sin(2*pi*(4*x - 9*y)) + sin(2*pi*(9*x - 4*y)) - sin(2*pi*(5*x - 9*y)) - sin(2*pi*(9*x - 5*y))
        FB += SF.ai[idx_a]*fB54*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([5,4])
        idx_a += 1

    if 24 in usedBasis:
        fA63 = cos(6*pi*(3*x - y)) + cos(6*pi*(2*x - 3*y)) + cos(6*pi*(3*x - 2*y)) + cos(6*pi*(x + 2*y)) + cos(6*pi*(2*x + y)) + cos(6*pi*(x - 3*y))
        FA += SF.ai[idx_a]*fA63*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB63 = sin(6*pi*(3*x - y)) - sin(6*pi*(2*x - 3*y)) - sin(6*pi*(3*x - 2*y)) - sin(6*pi*(x + 2*y)) + sin(6*pi*(2*x + y)) + sin(6*pi*(x - 3*y))
        FB += SF.ai[idx_a]*fB63*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([6,3])
        idx_a += 1

    if 25 in usedBasis:
        fA80 = 2*cos(16*x*pi) + 2*cos(16*y*pi) + 2*cos(16*pi*(x - y))
        FA += SF.ai[idx_a]*fA80*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB80 = 2*sin(16*x*pi) - 2*sin(16*y*pi) - 2*sin(16*pi*(x - y))
        FB += SF.ai[idx_a]*fB80*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([8,0])
        idx_a += 1

    if 26 in usedBasis:
        fA72 = cos(2*pi*(2*x + 7*y)) + cos(2*pi*(7*x + 2*y)) + cos(2*pi*(2*x - 9*y)) + cos(2*pi*(9*x - 2*y)) + cos(2*pi*(7*x - 9*y)) + cos(2*pi*(9*x - 7*y))
        FA += SF.ai[idx_a]*fA72*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB72 = sin(2*pi*(7*x + 2*y)) - sin(2*pi*(2*x + 7*y)) + sin(2*pi*(2*x - 9*y)) + sin(2*pi*(9*x - 2*y)) - sin(2*pi*(7*x - 9*y)) - sin(2*pi*(9*x - 7*y))
        FB += SF.ai[idx_a]*fB72*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([7,2])
        idx_a += 1

    if 27 in usedBasis:
        fA81 = cos(2*pi*(9*x - y)) + cos(2*pi*(8*x - 9*y)) + cos(2*pi*(9*x - 8*y)) + cos(2*pi*(x + 8*y)) + cos(2*pi*(8*x + y)) + cos(2*pi*(x - 9*y))
        FA += SF.ai[idx_a]*fA81*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB81 = sin(2*pi*(9*x - y)) - sin(2*pi*(8*x - 9*y)) - sin(2*pi*(9*x - 8*y)) - sin(2*pi*(x + 8*y)) + sin(2*pi*(8*x + y)) + sin(2*pi*(x - 9*y))
        FB += SF.ai[idx_a]*fB81*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([8,1])
        idx_a += 1

    if 28 in usedBasis:
        fA55 = 2*cos(10*pi*(2*x - y)) + 2*cos(10*pi*(x + y)) + 2*cos(10*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA55*Multi[idx_a]
        hk.append([5,5])
        idx_a += 1

    if 29 in usedBasis:
        fA64 = cos(4*pi*(2*x + 3*y)) + cos(4*pi*(3*x + 2*y)) + cos(4*pi*(2*x - 5*y)) + cos(4*pi*(5*x - 2*y)) + cos(4*pi*(3*x - 5*y)) + cos(4*pi*(5*x - 3*y))
        FA += SF.ai[idx_a]*fA64*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB64 = sin(4*pi*(3*x + 2*y)) - sin(4*pi*(2*x + 3*y)) + sin(4*pi*(2*x - 5*y)) + sin(4*pi*(5*x - 2*y)) - sin(4*pi*(3*x - 5*y)) - sin(4*pi*(5*x - 3*y))
        FB += SF.ai[idx_a]*fB64*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([6,4])
        idx_a += 1

    if 30 in usedBasis:
        fA73 = cos(2*pi*(3*x + 7*y)) + cos(2*pi*(7*x + 3*y)) + cos(2*pi*(3*x - 10*y)) + cos(2*pi*(10*x - 3*y)) + cos(2*pi*(7*x - 10*y)) + cos(2*pi*(10*x - 7*y))
        FA += SF.ai[idx_a]*fA73*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB73 = sin(2*pi*(7*x + 3*y)) - sin(2*pi*(3*x + 7*y)) + sin(2*pi*(3*x - 10*y)) + sin(2*pi*(10*x - 3*y)) - sin(2*pi*(7*x - 10*y)) - sin(2*pi*(10*x - 7*y))
        FB += SF.ai[idx_a]*fB73*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([7,3])
        idx_a += 1

    if 31 in usedBasis:
        fA90 = 2*cos(18*x*pi) + 2*cos(18*y*pi) + 2*cos(18*pi*(x - y))
        FA += SF.ai[idx_a]*fA90*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB90 = 2*sin(18*x*pi) - 2*sin(18*y*pi) - 2*sin(18*pi*(x - y))
        FB += SF.ai[idx_a]*fB90*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hk.append([9,0])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 1 0 1 1 1 0 1 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 0 1 1 1 
    # 314: [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    return FA+FB, idx_theta, hk
