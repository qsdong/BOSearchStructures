# Generated at 2024-03-12 09:09:38
# Qingshu Dong

import numpy as np

def  calF_143_2d0(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([2, 2, 6, 12, 2, 12, 12, 6, 2, 12, 12, 6, 12, 12, 12, 2, 12, 12, 12, 12, 2, 12, 12, 24, 12, 24, 12, 24, 12, 6, 12, 2])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 143.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA001 = 3*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA001*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB001 = 3*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB001*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,1])
        idx_a += 1

    if 1 in usedBasis:
        fA002 = 3*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA002*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB002 = 3*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB002*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,2])
        idx_a += 1

    if 2 in usedBasis:
        fA100 = cos(2*x*pi) + cos(2*y*pi) + cos(2*pi*(x - y))
        FA += SF.ai[idx_a]*fA100*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB100 = sin(2*x*pi) - sin(2*y*pi) - sin(2*pi*(x - y))
        FB += SF.ai[idx_a]*fB100*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,0])
        idx_a += 1

    if 3 in usedBasis:
        fA101 = cos(2*pi*(y - x + z)) + cos(2*pi*(x + z)) + cos(2*pi*(y - z))
        FA += SF.ai[idx_a]*fA101*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB101 = sin(2*pi*(y - x + z)) + sin(2*pi*(x + z)) - sin(2*pi*(y - z))
        FB += SF.ai[idx_a]*fB101*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,1])
        idx_a += 1

    if 4 in usedBasis:
        fA003 = 3*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA003*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB003 = 3*sin(6*z*pi)
        FB += SF.ai[idx_a]*fB003*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,3])
        idx_a += 1

    if 5 in usedBasis:
        fA102 = cos(2*pi*(y - x + 2*z)) + cos(2*pi*(x + 2*z)) + cos(2*pi*(y - 2*z))
        FA += SF.ai[idx_a]*fA102*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB102 = sin(2*pi*(y - x + 2*z)) + sin(2*pi*(x + 2*z)) - sin(2*pi*(y - 2*z))
        FB += SF.ai[idx_a]*fB102*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,2])
        idx_a += 1

    if 6 in usedBasis:
        fA103 = cos(2*pi*(y - x + 3*z)) + cos(2*pi*(x + 3*z)) + cos(2*pi*(y - 3*z))
        FA += SF.ai[idx_a]*fA103*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB103 = sin(2*pi*(y - x + 3*z)) + sin(2*pi*(x + 3*z)) - sin(2*pi*(y - 3*z))
        FB += SF.ai[idx_a]*fB103*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,3])
        idx_a += 1

    if 7 in usedBasis:
        fA110 = cos(2*pi*(2*x - y)) + cos(2*pi*(x + y)) + cos(2*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA110*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB110 = sin(2*pi*(x + y)) - sin(2*pi*(2*x - y)) + sin(2*pi*(x - 2*y))
        FB += SF.ai[idx_a]*fB110*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,0])
        idx_a += 1

    if 8 in usedBasis:
        fA004 = 3*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA004*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB004 = 3*sin(8*z*pi)
        FB += SF.ai[idx_a]*fB004*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,4])
        idx_a += 1

    if 9 in usedBasis:
        fA111 = cos(2*pi*(x - 2*y + z)) + cos(2*pi*(y - 2*x + z)) + cos(2*pi*(x + y + z))
        FA += SF.ai[idx_a]*fA111*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB111 = sin(2*pi*(x - 2*y + z)) + sin(2*pi*(y - 2*x + z)) + sin(2*pi*(x + y + z))
        FB += SF.ai[idx_a]*fB111*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,1])
        idx_a += 1

    if 10 in usedBasis:
        fA112 = cos(2*pi*(x + y + 2*z)) + cos(2*pi*(x - 2*y + 2*z)) + cos(2*pi*(y - 2*x + 2*z))
        FA += SF.ai[idx_a]*fA112*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB112 = sin(2*pi*(x + y + 2*z)) + sin(2*pi*(x - 2*y + 2*z)) + sin(2*pi*(y - 2*x + 2*z))
        FB += SF.ai[idx_a]*fB112*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,2])
        idx_a += 1

    if 11 in usedBasis:
        fA200 = cos(4*x*pi) + cos(4*y*pi) + cos(4*pi*(x - y))
        FA += SF.ai[idx_a]*fA200*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB200 = sin(4*x*pi) - sin(4*y*pi) - sin(4*pi*(x - y))
        FB += SF.ai[idx_a]*fB200*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,0])
        idx_a += 1

    if 12 in usedBasis:
        fA104 = cos(2*pi*(y - x + 4*z)) + cos(2*pi*(x + 4*z)) + cos(2*pi*(y - 4*z))
        FA += SF.ai[idx_a]*fA104*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB104 = sin(2*pi*(y - x + 4*z)) + sin(2*pi*(x + 4*z)) - sin(2*pi*(y - 4*z))
        FB += SF.ai[idx_a]*fB104*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,4])
        idx_a += 1

    if 13 in usedBasis:
        fA201 = cos(2*pi*(2*y - z)) + cos(2*pi*(2*y - 2*x + z)) + cos(2*pi*(2*x + z))
        FA += SF.ai[idx_a]*fA201*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB201 = sin(2*pi*(2*y - 2*x + z)) - sin(2*pi*(2*y - z)) + sin(2*pi*(2*x + z))
        FB += SF.ai[idx_a]*fB201*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,1])
        idx_a += 1

    if 14 in usedBasis:
        fA113 = cos(2*pi*(x + y + 3*z)) + cos(2*pi*(x - 2*y + 3*z)) + cos(2*pi*(y - 2*x + 3*z))
        FA += SF.ai[idx_a]*fA113*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB113 = sin(2*pi*(x + y + 3*z)) + sin(2*pi*(x - 2*y + 3*z)) + sin(2*pi*(y - 2*x + 3*z))
        FB += SF.ai[idx_a]*fB113*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,3])
        idx_a += 1

    if 15 in usedBasis:
        fA005 = 3*cos(10*z*pi)
        FA += SF.ai[idx_a]*fA005*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB005 = 3*sin(10*z*pi)
        FB += SF.ai[idx_a]*fB005*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,5])
        idx_a += 1

    if 16 in usedBasis:
        fA202 = cos(4*pi*(y - x + z)) + cos(4*pi*(x + z)) + cos(4*pi*(y - z))
        FA += SF.ai[idx_a]*fA202*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB202 = sin(4*pi*(y - x + z)) + sin(4*pi*(x + z)) - sin(4*pi*(y - z))
        FB += SF.ai[idx_a]*fB202*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,2])
        idx_a += 1

    if 17 in usedBasis:
        fA203 = cos(2*pi*(2*x + 3*z)) + cos(2*pi*(2*y - 3*z)) + cos(2*pi*(2*y - 2*x + 3*z))
        FA += SF.ai[idx_a]*fA203*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB203 = sin(2*pi*(2*y - 2*x + 3*z)) + sin(2*pi*(2*x + 3*z)) - sin(2*pi*(2*y - 3*z))
        FB += SF.ai[idx_a]*fB203*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,3])
        idx_a += 1

    if 18 in usedBasis:
        fA105 = cos(2*pi*(y - x + 5*z)) + cos(2*pi*(x + 5*z)) + cos(2*pi*(y - 5*z))
        FA += SF.ai[idx_a]*fA105*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB105 = sin(2*pi*(y - x + 5*z)) + sin(2*pi*(x + 5*z)) - sin(2*pi*(y - 5*z))
        FB += SF.ai[idx_a]*fB105*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,5])
        idx_a += 1

    if 19 in usedBasis:
        fA114 = cos(2*pi*(x + y + 4*z)) + cos(2*pi*(x - 2*y + 4*z)) + cos(2*pi*(y - 2*x + 4*z))
        FA += SF.ai[idx_a]*fA114*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB114 = sin(2*pi*(x + y + 4*z)) + sin(2*pi*(x - 2*y + 4*z)) + sin(2*pi*(y - 2*x + 4*z))
        FB += SF.ai[idx_a]*fB114*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,4])
        idx_a += 1

    if 20 in usedBasis:
        fA006 = 3*cos(12*z*pi)
        FA += SF.ai[idx_a]*fA006*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB006 = 3*sin(12*z*pi)
        FB += SF.ai[idx_a]*fB006*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,6])
        idx_a += 1

    if 21 in usedBasis:
        fA210 = cos(2*pi*(3*x - 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y))
        FA += SF.ai[idx_a]*fA210*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB210 = sin(2*pi*(2*x + y)) - sin(2*pi*(3*x - 2*y)) + sin(2*pi*(x - 3*y))
        FB += SF.ai[idx_a]*fB210*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,0])
        idx_a += 1

    if 22 in usedBasis:
        fA204 = cos(4*pi*(y - x + 2*z)) + cos(4*pi*(x + 2*z)) + cos(4*pi*(y - 2*z))
        FA += SF.ai[idx_a]*fA204*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB204 = sin(4*pi*(y - x + 2*z)) + sin(4*pi*(x + 2*z)) - sin(4*pi*(y - 2*z))
        FB += SF.ai[idx_a]*fB204*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,4])
        idx_a += 1

    if 23 in usedBasis:
        fA211 = cos(2*pi*(2*x + y + z)) + cos(2*pi*(x - 3*y + z)) + cos(2*pi*(2*y - 3*x + z))
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = sin(2*pi*(2*x + y + z)) + sin(2*pi*(x - 3*y + z)) + sin(2*pi*(2*y - 3*x + z))
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 24 in usedBasis:
        fA115 = cos(2*pi*(x + y + 5*z)) + cos(2*pi*(x - 2*y + 5*z)) + cos(2*pi*(y - 2*x + 5*z))
        FA += SF.ai[idx_a]*fA115*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB115 = sin(2*pi*(x + y + 5*z)) + sin(2*pi*(x - 2*y + 5*z)) + sin(2*pi*(y - 2*x + 5*z))
        FB += SF.ai[idx_a]*fB115*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,5])
        idx_a += 1

    if 25 in usedBasis:
        fA212 = cos(2*pi*(2*x + y + 2*z)) + cos(2*pi*(x - 3*y + 2*z)) + cos(2*pi*(2*y - 3*x + 2*z))
        FA += SF.ai[idx_a]*fA212*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB212 = sin(2*pi*(2*y - 3*x + 2*z)) + sin(2*pi*(2*x + y + 2*z)) + sin(2*pi*(x - 3*y + 2*z))
        FB += SF.ai[idx_a]*fB212*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,2])
        idx_a += 1

    if 26 in usedBasis:
        fA106 = cos(2*pi*(y - x + 6*z)) + cos(2*pi*(x + 6*z)) + cos(2*pi*(y - 6*z))
        FA += SF.ai[idx_a]*fA106*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB106 = sin(2*pi*(y - x + 6*z)) + sin(2*pi*(x + 6*z)) - sin(2*pi*(y - 6*z))
        FB += SF.ai[idx_a]*fB106*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,6])
        idx_a += 1

    if 27 in usedBasis:
        fA213 = cos(2*pi*(2*x + y + 3*z)) + cos(2*pi*(x - 3*y + 3*z)) + cos(2*pi*(2*y - 3*x + 3*z))
        FA += SF.ai[idx_a]*fA213*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB213 = sin(2*pi*(2*y - 3*x + 3*z)) + sin(2*pi*(2*x + y + 3*z)) + sin(2*pi*(x - 3*y + 3*z))
        FB += SF.ai[idx_a]*fB213*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,3])
        idx_a += 1

    if 28 in usedBasis:
        fA205 = cos(2*pi*(2*x + 5*z)) + cos(2*pi*(2*y - 5*z)) + cos(2*pi*(2*y - 2*x + 5*z))
        FA += SF.ai[idx_a]*fA205*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB205 = sin(2*pi*(2*y - 2*x + 5*z)) + sin(2*pi*(2*x + 5*z)) - sin(2*pi*(2*y - 5*z))
        FB += SF.ai[idx_a]*fB205*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,5])
        idx_a += 1

    if 29 in usedBasis:
        fA300 = cos(6*x*pi) + cos(6*y*pi) + cos(6*pi*(x - y))
        FA += SF.ai[idx_a]*fA300*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB300 = sin(6*x*pi) - sin(6*y*pi) - sin(6*pi*(x - y))
        FB += SF.ai[idx_a]*fB300*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,0])
        idx_a += 1

    if 30 in usedBasis:
        fA301 = cos(2*pi*(3*y - z)) + cos(2*pi*(3*y - 3*x + z)) + cos(2*pi*(3*x + z))
        FA += SF.ai[idx_a]*fA301*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB301 = sin(2*pi*(3*y - 3*x + z)) - sin(2*pi*(3*y - z)) + sin(2*pi*(3*x + z))
        FB += SF.ai[idx_a]*fB301*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,1])
        idx_a += 1

    if 31 in usedBasis:
        fA007 = 3*cos(14*z*pi)
        FA += SF.ai[idx_a]*fA007*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB007 = 3*sin(14*z*pi)
        FB += SF.ai[idx_a]*fB007*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,7])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 143_2d0: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    return FA+FB, idx_theta, hkl
