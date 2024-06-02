# Generated at 2024-03-12 14:36:00
# Qingshu Dong

import numpy as np

def  calF_161(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([6, 12, 24, 6, 12, 6, 12, 24, 12, 24, 24, 12, 6, 2, 24, 12, 12, 12, 24, 24, 24, 24, 12, 6, 12, 24, 12, 12, 24, 24, 24, 24])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 161.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA110 = 6*cos(2*pi*(2*x - y)) + 6*cos(2*pi*(x + y)) + 6*cos(2*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 1 in usedBasis:
        fA202 = 6*cos(4*pi*(y - x + z)) + 6*cos(4*pi*(x + z)) + 6*cos(4*pi*(y - z))
        FA += SF.ai[idx_a]*fA202*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB202 = 6*sin(4*pi*(y - x + z)) + 6*sin(4*pi*(x + z)) - 6*sin(4*pi*(y - z))
        FB += SF.ai[idx_a]*fB202*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,2])
        idx_a += 1

    if 2 in usedBasis:
        fA211 = 3*cos(2*pi*(2*x + y + z)) + 3*cos(2*pi*(x - 3*y + z)) - 3*cos(2*pi*(x + 2*y - z)) - 3*cos(2*pi*(3*x - y + z)) - 3*cos(2*pi*(3*y - 2*x + z)) + 3*cos(2*pi*(2*y - 3*x + z))
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = 3*sin(2*pi*(2*x + y + z)) + 3*sin(2*pi*(x - 3*y + z)) + 3*sin(2*pi*(x + 2*y - z)) - 3*sin(2*pi*(3*x - y + z)) - 3*sin(2*pi*(3*y - 2*x + z)) + 3*sin(2*pi*(2*y - 3*x + z))
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 3 in usedBasis:
        fA300 = 6*cos(6*x*pi) + 6*cos(6*y*pi) + 6*cos(6*pi*(x - y))
        FA += SF.ai[idx_a]*fA300*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB300 = 6*sin(6*x*pi) - 6*sin(6*y*pi) - 6*sin(6*pi*(x - y))
        FB += SF.ai[idx_a]*fB300*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,0])
        idx_a += 1

    if 4 in usedBasis:
        fA113 = -6*sin(6*z*pi)*(sin(2*pi*(x + y)) - sin(2*pi*(2*x - y)) + sin(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA113*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB113 = 6*cos(6*z*pi)*(sin(2*pi*(x + y)) - sin(2*pi*(2*x - y)) + sin(2*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB113*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,3])
        idx_a += 1

    if 5 in usedBasis:
        fA220 = 6*cos(4*pi*(2*x - y)) + 6*cos(4*pi*(x + y)) + 6*cos(4*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 6 in usedBasis:
        fA104 = 6*cos(2*pi*(y - x + 4*z)) + 6*cos(2*pi*(x + 4*z)) + 6*cos(2*pi*(y - 4*z))
        FA += SF.ai[idx_a]*fA104*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB104 = 6*sin(2*pi*(y - x + 4*z)) + 6*sin(2*pi*(x + 4*z)) - 6*sin(2*pi*(y - 4*z))
        FB += SF.ai[idx_a]*fB104*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,4])
        idx_a += 1

    if 7 in usedBasis:
        fA312 = 3*cos(2*pi*(x + 3*y - 2*z)) + 3*cos(2*pi*(3*x + y + 2*z)) + 3*cos(2*pi*(x - 4*y + 2*z)) + 3*cos(2*pi*(4*x - y + 2*z)) + 3*cos(2*pi*(4*y - 3*x + 2*z)) + 3*cos(2*pi*(3*y - 4*x + 2*z))
        FA += SF.ai[idx_a]*fA312*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB312 = 3*sin(2*pi*(4*x - y + 2*z)) + 3*sin(2*pi*(4*y - 3*x + 2*z)) + 3*sin(2*pi*(3*y - 4*x + 2*z)) - 3*sin(2*pi*(x + 3*y - 2*z)) + 3*sin(2*pi*(3*x + y + 2*z)) + 3*sin(2*pi*(x - 4*y + 2*z))
        FB += SF.ai[idx_a]*fB312*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,2])
        idx_a += 1

    if 8 in usedBasis:
        fA223 = -6*sin(6*z*pi)*(sin(4*pi*(x + y)) - sin(4*pi*(2*x - y)) + sin(4*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA223*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB223 = 6*cos(6*z*pi)*(sin(4*pi*(x + y)) - sin(4*pi*(2*x - y)) + sin(4*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB223*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,3])
        idx_a += 1

    if 9 in usedBasis:
        fA214 = 3*cos(2*pi*(x + 2*y - 4*z)) + 3*cos(2*pi*(2*x + y + 4*z)) + 3*cos(2*pi*(x - 3*y + 4*z)) + 3*cos(2*pi*(3*x - y + 4*z)) + 3*cos(2*pi*(3*y - 2*x + 4*z)) + 3*cos(2*pi*(2*y - 3*x + 4*z))
        FA += SF.ai[idx_a]*fA214*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB214 = 3*sin(2*pi*(3*x - y + 4*z)) + 3*sin(2*pi*(3*y - 2*x + 4*z)) + 3*sin(2*pi*(2*y - 3*x + 4*z)) - 3*sin(2*pi*(x + 2*y - 4*z)) + 3*sin(2*pi*(2*x + y + 4*z)) + 3*sin(2*pi*(x - 3*y + 4*z))
        FB += SF.ai[idx_a]*fB214*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,4])
        idx_a += 1

    if 10 in usedBasis:
        fA321 = 3*cos(2*pi*(3*x + 2*y + z)) + 3*cos(2*pi*(2*x - 5*y + z)) - 3*cos(2*pi*(5*x - 2*y + z)) - 3*cos(2*pi*(5*y - 3*x + z)) + 3*cos(2*pi*(3*y - 5*x + z)) - 3*cos(2*pi*(2*x + 3*y - z))
        FA += SF.ai[idx_a]*fA321*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB321 = 3*sin(2*pi*(2*x + 3*y - z)) + 3*sin(2*pi*(3*x + 2*y + z)) + 3*sin(2*pi*(2*x - 5*y + z)) - 3*sin(2*pi*(5*x - 2*y + z)) - 3*sin(2*pi*(5*y - 3*x + z)) + 3*sin(2*pi*(3*y - 5*x + z))
        FB += SF.ai[idx_a]*fB321*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,1])
        idx_a += 1

    if 11 in usedBasis:
        fA410 = 3*cos(2*pi*(5*x - y)) + 3*cos(2*pi*(4*x - 5*y)) + 3*cos(2*pi*(5*x - 4*y)) + 3*cos(2*pi*(x + 4*y)) + 3*cos(2*pi*(4*x + y)) + 3*cos(2*pi*(x - 5*y))
        FA += SF.ai[idx_a]*fA410*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB410 = 3*sin(2*pi*(5*x - y)) - 3*sin(2*pi*(4*x - 5*y)) - 3*sin(2*pi*(5*x - 4*y)) - 3*sin(2*pi*(x + 4*y)) + 3*sin(2*pi*(4*x + y)) + 3*sin(2*pi*(x - 5*y))
        FB += SF.ai[idx_a]*fB410*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,1,0])
        idx_a += 1

    if 12 in usedBasis:
        fA330 = 6*cos(6*pi*(2*x - y)) + 6*cos(6*pi*(x + y)) + 6*cos(6*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA330*Multi[idx_a]
        hkl.append([3,3,0])
        idx_a += 1

    if 13 in usedBasis:
        fA006 = 18*cos(12*z*pi)
        FA += SF.ai[idx_a]*fA006*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB006 = 18*sin(12*z*pi)
        FB += SF.ai[idx_a]*fB006*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,6])
        idx_a += 1

    if 14 in usedBasis:
        fA413 = 3*cos(2*pi*(4*x + y + 3*z)) - 3*cos(2*pi*(x + 4*y - 3*z)) + 3*cos(2*pi*(x - 5*y + 3*z)) - 3*cos(2*pi*(5*x - y + 3*z)) - 3*cos(2*pi*(5*y - 4*x + 3*z)) + 3*cos(2*pi*(4*y - 5*x + 3*z))
        FA += SF.ai[idx_a]*fA413*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB413 = 3*sin(2*pi*(4*y - 5*x + 3*z)) - 3*sin(2*pi*(5*y - 4*x + 3*z)) - 3*sin(2*pi*(5*x - y + 3*z)) + 3*sin(2*pi*(x + 4*y - 3*z)) + 3*sin(2*pi*(4*x + y + 3*z)) + 3*sin(2*pi*(x - 5*y + 3*z))
        FB += SF.ai[idx_a]*fB413*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,1,3])
        idx_a += 1

    if 15 in usedBasis:
        fA502 = 6*cos(2*pi*(5*x + 2*z)) + 6*cos(2*pi*(5*y - 2*z)) + 6*cos(2*pi*(5*y - 5*x + 2*z))
        FA += SF.ai[idx_a]*fA502*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB502 = 6*sin(2*pi*(5*y - 5*x + 2*z)) + 6*sin(2*pi*(5*x + 2*z)) - 6*sin(2*pi*(5*y - 2*z))
        FB += SF.ai[idx_a]*fB502*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,0,2])
        idx_a += 1

    if 16 in usedBasis:
        fA404 = 6*cos(8*pi*(y - x + z)) + 6*cos(8*pi*(x + z)) + 6*cos(8*pi*(y - z))
        FA += SF.ai[idx_a]*fA404*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB404 = 6*sin(8*pi*(y - x + z)) + 6*sin(8*pi*(x + z)) - 6*sin(8*pi*(y - z))
        FB += SF.ai[idx_a]*fB404*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,0,4])
        idx_a += 1

    if 17 in usedBasis:
        fA116 = 6*cos(12*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA116*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB116 = 6*sin(12*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB116*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,6])
        idx_a += 1

    if 18 in usedBasis:
        fA422 = 3*cos(4*pi*(2*x + y + z)) + 3*cos(4*pi*(x - 3*y + z)) + 3*cos(4*pi*(x + 2*y - z)) + 3*cos(4*pi*(3*x - y + z)) + 3*cos(4*pi*(3*y - 2*x + z)) + 3*cos(4*pi*(2*y - 3*x + z))
        FA += SF.ai[idx_a]*fA422*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB422 = 3*sin(4*pi*(2*x + y + z)) + 3*sin(4*pi*(x - 3*y + z)) - 3*sin(4*pi*(x + 2*y - z)) + 3*sin(4*pi*(3*x - y + z)) + 3*sin(4*pi*(3*y - 2*x + z)) + 3*sin(4*pi*(2*y - 3*x + z))
        FB += SF.ai[idx_a]*fB422*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,2,2])
        idx_a += 1

    if 19 in usedBasis:
        fA324 = 3*cos(2*pi*(2*x + 3*y - 4*z)) + 3*cos(2*pi*(3*x + 2*y + 4*z)) + 3*cos(2*pi*(2*x - 5*y + 4*z)) + 3*cos(2*pi*(5*x - 2*y + 4*z)) + 3*cos(2*pi*(5*y - 3*x + 4*z)) + 3*cos(2*pi*(3*y - 5*x + 4*z))
        FA += SF.ai[idx_a]*fA324*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB324 = 3*sin(2*pi*(3*x + 2*y + 4*z)) - 3*sin(2*pi*(2*x + 3*y - 4*z)) + 3*sin(2*pi*(2*x - 5*y + 4*z)) + 3*sin(2*pi*(5*x - 2*y + 4*z)) + 3*sin(2*pi*(5*y - 3*x + 4*z)) + 3*sin(2*pi*(3*y - 5*x + 4*z))
        FB += SF.ai[idx_a]*fB324*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,4])
        idx_a += 1

    if 20 in usedBasis:
        fA511 = 3*cos(2*pi*(5*x + y + z)) + 3*cos(2*pi*(x - 6*y + z)) - 3*cos(2*pi*(x + 5*y - z)) - 3*cos(2*pi*(6*x - y + z)) - 3*cos(2*pi*(6*y - 5*x + z)) + 3*cos(2*pi*(5*y - 6*x + z))
        FA += SF.ai[idx_a]*fA511*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB511 = 3*sin(2*pi*(5*x + y + z)) + 3*sin(2*pi*(x - 6*y + z)) + 3*sin(2*pi*(x + 5*y - z)) - 3*sin(2*pi*(6*x - y + z)) - 3*sin(2*pi*(6*y - 5*x + z)) + 3*sin(2*pi*(5*y - 6*x + z))
        FB += SF.ai[idx_a]*fB511*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,1,1])
        idx_a += 1

    if 21 in usedBasis:
        fA315 = 3*cos(2*pi*(3*x + y + 5*z)) - 3*cos(2*pi*(x + 3*y - 5*z)) + 3*cos(2*pi*(x - 4*y + 5*z)) - 3*cos(2*pi*(4*x - y + 5*z)) - 3*cos(2*pi*(4*y - 3*x + 5*z)) + 3*cos(2*pi*(3*y - 4*x + 5*z))
        FA += SF.ai[idx_a]*fA315*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB315 = 3*sin(2*pi*(3*y - 4*x + 5*z)) - 3*sin(2*pi*(4*y - 3*x + 5*z)) - 3*sin(2*pi*(4*x - y + 5*z)) + 3*sin(2*pi*(x + 3*y - 5*z)) + 3*sin(2*pi*(3*x + y + 5*z)) + 3*sin(2*pi*(x - 4*y + 5*z))
        FB += SF.ai[idx_a]*fB315*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,5])
        idx_a += 1

    if 22 in usedBasis:
        fA333 = -6*sin(6*z*pi)*(sin(6*pi*(x + y)) - sin(6*pi*(2*x - y)) + sin(6*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA333*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB333 = 6*cos(6*z*pi)*(sin(6*pi*(x + y)) - sin(6*pi*(2*x - y)) + sin(6*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB333*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,3,3])
        idx_a += 1

    if 23 in usedBasis:
        fA600 = 6*cos(12*x*pi) + 6*cos(12*y*pi) + 6*cos(12*pi*(x - y))
        FA += SF.ai[idx_a]*fA600*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB600 = 6*sin(12*x*pi) - 6*sin(12*y*pi) - 6*sin(12*pi*(x - y))
        FB += SF.ai[idx_a]*fB600*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,0,0])
        idx_a += 1

    if 24 in usedBasis:
        fA306 = 6*cos(6*pi*(y - x + 2*z)) + 6*cos(6*pi*(x + 2*z)) + 6*cos(6*pi*(y - 2*z))
        FA += SF.ai[idx_a]*fA306*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB306 = 6*sin(6*pi*(y - x + 2*z)) + 6*sin(6*pi*(x + 2*z)) - 6*sin(6*pi*(y - 2*z))
        FB += SF.ai[idx_a]*fB306*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,6])
        idx_a += 1

    if 25 in usedBasis:
        fA431 = 3*cos(2*pi*(4*x + 3*y + z)) + 3*cos(2*pi*(3*x - 7*y + z)) - 3*cos(2*pi*(7*x - 3*y + z)) - 3*cos(2*pi*(7*y - 4*x + z)) + 3*cos(2*pi*(4*y - 7*x + z)) - 3*cos(2*pi*(3*x + 4*y - z))
        FA += SF.ai[idx_a]*fA431*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB431 = 3*sin(2*pi*(3*x + 4*y - z)) + 3*sin(2*pi*(4*x + 3*y + z)) + 3*sin(2*pi*(3*x - 7*y + z)) - 3*sin(2*pi*(7*x - 3*y + z)) - 3*sin(2*pi*(7*y - 4*x + z)) + 3*sin(2*pi*(4*y - 7*x + z))
        FB += SF.ai[idx_a]*fB431*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,3,1])
        idx_a += 1

    if 26 in usedBasis:
        fA520 = 3*cos(2*pi*(2*x + 5*y)) + 3*cos(2*pi*(5*x + 2*y)) + 3*cos(2*pi*(2*x - 7*y)) + 3*cos(2*pi*(7*x - 2*y)) + 3*cos(2*pi*(5*x - 7*y)) + 3*cos(2*pi*(7*x - 5*y))
        FA += SF.ai[idx_a]*fA520*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB520 = 3*sin(2*pi*(5*x + 2*y)) - 3*sin(2*pi*(2*x + 5*y)) + 3*sin(2*pi*(2*x - 7*y)) + 3*sin(2*pi*(7*x - 2*y)) - 3*sin(2*pi*(5*x - 7*y)) - 3*sin(2*pi*(7*x - 5*y))
        FB += SF.ai[idx_a]*fB520*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,2,0])
        idx_a += 1

    if 27 in usedBasis:
        fA226 = 6*cos(12*z*pi)*(cos(4*pi*(2*x - y)) + cos(4*pi*(x + y)) + cos(4*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA226*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB226 = 6*sin(12*z*pi)*(cos(4*pi*(2*x - y)) + cos(4*pi*(x + y)) + cos(4*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB226*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,6])
        idx_a += 1

    if 28 in usedBasis:
        fA514 = 3*cos(2*pi*(x + 5*y - 4*z)) + 3*cos(2*pi*(5*x + y + 4*z)) + 3*cos(2*pi*(x - 6*y + 4*z)) + 3*cos(2*pi*(6*x - y + 4*z)) + 3*cos(2*pi*(6*y - 5*x + 4*z)) + 3*cos(2*pi*(5*y - 6*x + 4*z))
        FA += SF.ai[idx_a]*fA514*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB514 = 3*sin(2*pi*(6*x - y + 4*z)) + 3*sin(2*pi*(6*y - 5*x + 4*z)) + 3*sin(2*pi*(5*y - 6*x + 4*z)) - 3*sin(2*pi*(x + 5*y - 4*z)) + 3*sin(2*pi*(5*x + y + 4*z)) + 3*sin(2*pi*(x - 6*y + 4*z))
        FB += SF.ai[idx_a]*fB514*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,1,4])
        idx_a += 1

    if 29 in usedBasis:
        fA217 = 3*cos(2*pi*(2*x + y + 7*z)) - 3*cos(2*pi*(x + 2*y - 7*z)) + 3*cos(2*pi*(x - 3*y + 7*z)) - 3*cos(2*pi*(3*x - y + 7*z)) - 3*cos(2*pi*(3*y - 2*x + 7*z)) + 3*cos(2*pi*(2*y - 3*x + 7*z))
        FA += SF.ai[idx_a]*fA217*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB217 = 3*sin(2*pi*(2*y - 3*x + 7*z)) - 3*sin(2*pi*(3*y - 2*x + 7*z)) - 3*sin(2*pi*(3*x - y + 7*z)) + 3*sin(2*pi*(x + 2*y - 7*z)) + 3*sin(2*pi*(2*x + y + 7*z)) + 3*sin(2*pi*(x - 3*y + 7*z))
        FB += SF.ai[idx_a]*fB217*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,7])
        idx_a += 1

    if 30 in usedBasis:
        fA523 = 3*cos(2*pi*(5*x + 2*y + 3*z)) - 3*cos(2*pi*(2*x + 5*y - 3*z)) + 3*cos(2*pi*(2*x - 7*y + 3*z)) - 3*cos(2*pi*(7*x - 2*y + 3*z)) - 3*cos(2*pi*(7*y - 5*x + 3*z)) + 3*cos(2*pi*(5*y - 7*x + 3*z))
        FA += SF.ai[idx_a]*fA523*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB523 = 3*sin(2*pi*(2*x + 5*y - 3*z)) + 3*sin(2*pi*(5*x + 2*y + 3*z)) + 3*sin(2*pi*(2*x - 7*y + 3*z)) - 3*sin(2*pi*(7*x - 2*y + 3*z)) - 3*sin(2*pi*(7*y - 5*x + 3*z)) + 3*sin(2*pi*(5*y - 7*x + 3*z))
        FB += SF.ai[idx_a]*fB523*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,2,3])
        idx_a += 1

    if 31 in usedBasis:
        fA612 = 3*cos(2*pi*(x + 6*y - 2*z)) + 3*cos(2*pi*(6*x + y + 2*z)) + 3*cos(2*pi*(x - 7*y + 2*z)) + 3*cos(2*pi*(7*x - y + 2*z)) + 3*cos(2*pi*(7*y - 6*x + 2*z)) + 3*cos(2*pi*(6*y - 7*x + 2*z))
        FA += SF.ai[idx_a]*fA612*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB612 = 3*sin(2*pi*(7*x - y + 2*z)) + 3*sin(2*pi*(7*y - 6*x + 2*z)) + 3*sin(2*pi*(6*y - 7*x + 2*z)) - 3*sin(2*pi*(x + 6*y - 2*z)) + 3*sin(2*pi*(6*x + y + 2*z)) + 3*sin(2*pi*(x - 7*y + 2*z))
        FB += SF.ai[idx_a]*fB612*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,1,2])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 161: [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    return FA+FB, idx_theta, hkl
