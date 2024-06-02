# Generated at 2024-02-23 18:30:34
# Qingshu Dong

import numpy as np

def  calF_186_2d0(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([2, 6, 12, 12, 12, 6, 2, 12, 6, 12, 12, 12, 12, 12, 12, 2, 12, 12, 24, 24, 12, 24, 12, 6, 12, 12, 12, 24, 12, 12, 12, 24])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 186.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA002 = 12*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA002*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB002 = 12*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB002*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,2])
        idx_a += 1

    if 1 in usedBasis:
        fA100 = 4*cos(2*x*pi) + 4*cos(2*y*pi) + 4*cos(2*pi*(x - y))
        FA += SF.ai[idx_a]*fA100*Multi[idx_a]
        hkl.append([1,0,0])
        idx_a += 1

    if 2 in usedBasis:
        fA101 = 4*sin(2*z*pi)*(sin(2*y*pi) - sin(2*x*pi) + sin(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA101*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB101 = -4*cos(2*z*pi)*(sin(2*y*pi) - sin(2*x*pi) + sin(2*pi*(x - y)))
        FB += SF.ai[idx_a]*fB101*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,1])
        idx_a += 1

    if 3 in usedBasis:
        fA102 = 4*cos(4*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA102*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB102 = 4*sin(4*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FB += SF.ai[idx_a]*fB102*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,2])
        idx_a += 1

    if 4 in usedBasis:
        fA103 = 4*sin(6*z*pi)*(sin(2*y*pi) - sin(2*x*pi) + sin(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA103*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB103 = -4*cos(6*z*pi)*(sin(2*y*pi) - sin(2*x*pi) + sin(2*pi*(x - y)))
        FB += SF.ai[idx_a]*fB103*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,3])
        idx_a += 1

    if 5 in usedBasis:
        fA110 = 4*cos(2*pi*(2*x - y)) + 4*cos(2*pi*(x + y)) + 4*cos(2*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 6 in usedBasis:
        fA004 = 12*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA004*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB004 = 12*sin(8*z*pi)
        FB += SF.ai[idx_a]*fB004*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,4])
        idx_a += 1

    if 7 in usedBasis:
        fA112 = 4*cos(4*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA112*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB112 = 4*sin(4*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB112*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,2])
        idx_a += 1

    if 8 in usedBasis:
        fA200 = 4*cos(4*x*pi) + 4*cos(4*y*pi) + 4*cos(4*pi*(x - y))
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 9 in usedBasis:
        fA104 = 4*cos(8*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA104*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB104 = 4*sin(8*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FB += SF.ai[idx_a]*fB104*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,4])
        idx_a += 1

    if 10 in usedBasis:
        fA201 = 4*sin(2*z*pi)*(sin(4*y*pi) - sin(4*x*pi) + sin(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA201*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB201 = -4*cos(2*z*pi)*(sin(4*y*pi) - sin(4*x*pi) + sin(4*pi*(x - y)))
        FB += SF.ai[idx_a]*fB201*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,1])
        idx_a += 1

    if 11 in usedBasis:
        fA202 = 4*cos(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA202*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB202 = 4*sin(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FB += SF.ai[idx_a]*fB202*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,2])
        idx_a += 1

    if 12 in usedBasis:
        fA203 = 4*sin(6*z*pi)*(sin(4*y*pi) - sin(4*x*pi) + sin(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA203*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB203 = -4*cos(6*z*pi)*(sin(4*y*pi) - sin(4*x*pi) + sin(4*pi*(x - y)))
        FB += SF.ai[idx_a]*fB203*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,3])
        idx_a += 1

    if 13 in usedBasis:
        fA105 = 4*sin(10*z*pi)*(sin(2*y*pi) - sin(2*x*pi) + sin(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA105*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB105 = -4*cos(10*z*pi)*(sin(2*y*pi) - sin(2*x*pi) + sin(2*pi*(x - y)))
        FB += SF.ai[idx_a]*fB105*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,5])
        idx_a += 1

    if 14 in usedBasis:
        fA114 = 4*cos(8*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA114*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB114 = 4*sin(8*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB114*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,4])
        idx_a += 1

    if 15 in usedBasis:
        fA006 = 12*cos(12*z*pi)
        FA += SF.ai[idx_a]*fA006*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB006 = 12*sin(12*z*pi)
        FB += SF.ai[idx_a]*fB006*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,6])
        idx_a += 1

    if 16 in usedBasis:
        fA210 = 2*cos(2*pi*(3*x - y)) + 2*cos(2*pi*(2*x - 3*y)) + 2*cos(2*pi*(3*x - 2*y)) + 2*cos(2*pi*(x + 2*y)) + 2*cos(2*pi*(2*x + y)) + 2*cos(2*pi*(x - 3*y))
        FA += SF.ai[idx_a]*fA210*Multi[idx_a]
        hkl.append([2,1,0])
        idx_a += 1

    if 17 in usedBasis:
        fA204 = 4*cos(8*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA204*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB204 = 4*sin(8*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FB += SF.ai[idx_a]*fB204*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,4])
        idx_a += 1

    if 18 in usedBasis:
        fA211 = -2*sin(2*z*pi)*(sin(2*pi*(3*x - y)) - sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - 2*y)) - sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = 2*cos(2*z*pi)*(sin(2*pi*(3*x - y)) - sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - 2*y)) - sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y)))
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 19 in usedBasis:
        fA212 = 2*cos(4*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA212*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB212 = 2*sin(4*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FB += SF.ai[idx_a]*fB212*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,2])
        idx_a += 1

    if 20 in usedBasis:
        fA106 = 4*cos(12*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA106*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB106 = 4*sin(12*z*pi)*(cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y)))
        FB += SF.ai[idx_a]*fB106*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,6])
        idx_a += 1

    if 21 in usedBasis:
        fA213 = -2*sin(6*z*pi)*(sin(2*pi*(3*x - y)) - sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - 2*y)) - sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA213*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB213 = 2*cos(6*z*pi)*(sin(2*pi*(3*x - y)) - sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - 2*y)) - sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y)))
        FB += SF.ai[idx_a]*fB213*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,3])
        idx_a += 1

    if 22 in usedBasis:
        fA205 = 4*sin(10*z*pi)*(sin(4*y*pi) - sin(4*x*pi) + sin(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA205*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB205 = -4*cos(10*z*pi)*(sin(4*y*pi) - sin(4*x*pi) + sin(4*pi*(x - y)))
        FB += SF.ai[idx_a]*fB205*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,5])
        idx_a += 1

    if 23 in usedBasis:
        fA300 = 4*cos(6*x*pi) + 4*cos(6*y*pi) + 4*cos(6*pi*(x - y))
        FA += SF.ai[idx_a]*fA300*Multi[idx_a]
        hkl.append([3,0,0])
        idx_a += 1

    if 24 in usedBasis:
        fA301 = 4*sin(2*z*pi)*(sin(6*y*pi) - sin(6*x*pi) + sin(6*pi*(x - y)))
        FA += SF.ai[idx_a]*fA301*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB301 = -4*cos(2*z*pi)*(sin(6*y*pi) - sin(6*x*pi) + sin(6*pi*(x - y)))
        FB += SF.ai[idx_a]*fB301*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,1])
        idx_a += 1

    if 25 in usedBasis:
        fA302 = 4*cos(4*z*pi)*(cos(6*x*pi) + cos(6*y*pi) + cos(6*pi*(x - y)))
        FA += SF.ai[idx_a]*fA302*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB302 = 4*sin(4*z*pi)*(cos(6*x*pi) + cos(6*y*pi) + cos(6*pi*(x - y)))
        FB += SF.ai[idx_a]*fB302*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,2])
        idx_a += 1

    if 26 in usedBasis:
        fA116 = 4*cos(12*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FA += SF.ai[idx_a]*fA116*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB116 = 4*sin(12*z*pi)*(cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y)))
        FB += SF.ai[idx_a]*fB116*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,6])
        idx_a += 1

    if 27 in usedBasis:
        fA214 = 2*cos(8*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA214*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB214 = 2*sin(8*z*pi)*(cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y)))
        FB += SF.ai[idx_a]*fB214*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,4])
        idx_a += 1

    if 28 in usedBasis:
        fA107 = 4*sin(14*z*pi)*(sin(2*y*pi) - sin(2*x*pi) + sin(2*pi*(x - y)))
        FA += SF.ai[idx_a]*fA107*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB107 = -4*cos(14*z*pi)*(sin(2*y*pi) - sin(2*x*pi) + sin(2*pi*(x - y)))
        FB += SF.ai[idx_a]*fB107*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,7])
        idx_a += 1

    if 29 in usedBasis:
        fA303 = 4*sin(6*z*pi)*(sin(6*y*pi) - sin(6*x*pi) + sin(6*pi*(x - y)))
        FA += SF.ai[idx_a]*fA303*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB303 = -4*cos(6*z*pi)*(sin(6*y*pi) - sin(6*x*pi) + sin(6*pi*(x - y)))
        FB += SF.ai[idx_a]*fB303*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,3])
        idx_a += 1

    if 30 in usedBasis:
        fA206 = 4*cos(12*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FA += SF.ai[idx_a]*fA206*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB206 = 4*sin(12*z*pi)*(cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y)))
        FB += SF.ai[idx_a]*fB206*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,6])
        idx_a += 1

    if 31 in usedBasis:
        fA215 = -2*sin(10*z*pi)*(sin(2*pi*(3*x - y)) - sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - 2*y)) - sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y)))
        FA += SF.ai[idx_a]*fA215*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB215 = 2*cos(10*z*pi)*(sin(2*pi*(3*x - y)) - sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - 2*y)) - sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y)))
        FB += SF.ai[idx_a]*fB215*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,5])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 1 0 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 
    # 186_2d0: [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    return FA+FB, idx_theta, hkl
