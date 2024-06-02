# Generated at 2024-02-26 11:13:21
# Qingshu Dong

import numpy as np

def  calF_115_2d0(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([2, 4, 2, 8, 4, 8, 8, 2, 8, 8, 4, 2, 8, 8, 8, 8, 8, 16, 16, 8, 8, 2, 16, 8, 4, 8, 8, 8, 4, 8, 16, 2])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 115.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA001 = 8*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA001*Multi[idx_a]
        hkl.append([0,0,1])
        idx_a += 1

    if 1 in usedBasis:
        fA100 = 4*cos(2*x*pi) + 4*cos(2*y*pi)
        FA += SF.ai[idx_a]*fA100*Multi[idx_a]
        hkl.append([1,0,0])
        idx_a += 1

    if 2 in usedBasis:
        fA002 = 8*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA002*Multi[idx_a]
        hkl.append([0,0,2])
        idx_a += 1

    if 3 in usedBasis:
        fA101 = 4*cos(2*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA101*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB101 = 4*sin(2*z*pi)*(cos(2*x*pi) - cos(2*y*pi))
        FB += SF.ai[idx_a]*fB101*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,1])
        idx_a += 1

    if 4 in usedBasis:
        fA110 = 8*cos(2*x*pi)*cos(2*y*pi)
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 5 in usedBasis:
        fA102 = 4*cos(4*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA102*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB102 = 4*sin(4*z*pi)*(cos(2*x*pi) - cos(2*y*pi))
        FB += SF.ai[idx_a]*fB102*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,2])
        idx_a += 1

    if 6 in usedBasis:
        fA111 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA111*Multi[idx_a]
        hkl.append([1,1,1])
        idx_a += 1

    if 7 in usedBasis:
        fA003 = 8*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA003*Multi[idx_a]
        hkl.append([0,0,3])
        idx_a += 1

    if 8 in usedBasis:
        fA112 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA112*Multi[idx_a]
        hkl.append([1,1,2])
        idx_a += 1

    if 9 in usedBasis:
        fA103 = 4*cos(6*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA103*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB103 = 4*sin(6*z*pi)*(cos(2*x*pi) - cos(2*y*pi))
        FB += SF.ai[idx_a]*fB103*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,3])
        idx_a += 1

    if 10 in usedBasis:
        fA200 = 4*cos(4*x*pi) + 4*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 11 in usedBasis:
        fA004 = 8*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA004*Multi[idx_a]
        hkl.append([0,0,4])
        idx_a += 1

    if 12 in usedBasis:
        fA201 = 4*cos(2*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA201*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB201 = 4*sin(2*z*pi)*(cos(4*x*pi) - cos(4*y*pi))
        FB += SF.ai[idx_a]*fB201*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,1])
        idx_a += 1

    if 13 in usedBasis:
        fA113 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA113*Multi[idx_a]
        hkl.append([1,1,3])
        idx_a += 1

    if 14 in usedBasis:
        fA210 = 4*cos(2*x*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA210*Multi[idx_a]
        hkl.append([2,1,0])
        idx_a += 1

    if 15 in usedBasis:
        fA202 = 4*cos(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA202*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB202 = 4*sin(4*z*pi)*(cos(4*x*pi) - cos(4*y*pi))
        FB += SF.ai[idx_a]*fB202*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,2])
        idx_a += 1

    if 16 in usedBasis:
        fA104 = 4*cos(8*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA104*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB104 = 4*sin(8*z*pi)*(cos(2*x*pi) - cos(2*y*pi))
        FB += SF.ai[idx_a]*fB104*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,4])
        idx_a += 1

    if 17 in usedBasis:
        fA211 = 4*cos(2*x*pi)*cos(2*z*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*cos(2*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = 4*cos(2*y*pi)*sin(2*z*pi)*(2*cos(2*x*pi)**2 - 1) - 4*cos(2*x*pi)*sin(2*z*pi)*(2*cos(2*y*pi)**2 - 1)
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 18 in usedBasis:
        fA212 = 4*cos(2*x*pi)*cos(4*z*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*cos(4*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA212*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB212 = 4*cos(2*y*pi)*sin(4*z*pi)*(2*cos(2*x*pi)**2 - 1) - 4*cos(2*x*pi)*sin(4*z*pi)*(2*cos(2*y*pi)**2 - 1)
        FB += SF.ai[idx_a]*fB212*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,2])
        idx_a += 1

    if 19 in usedBasis:
        fA114 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA114*Multi[idx_a]
        hkl.append([1,1,4])
        idx_a += 1

    if 20 in usedBasis:
        fA203 = 4*cos(6*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA203*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB203 = 4*sin(6*z*pi)*(cos(4*x*pi) - cos(4*y*pi))
        FB += SF.ai[idx_a]*fB203*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,3])
        idx_a += 1

    if 21 in usedBasis:
        fA005 = 8*cos(10*z*pi)
        FA += SF.ai[idx_a]*fA005*Multi[idx_a]
        hkl.append([0,0,5])
        idx_a += 1

    if 22 in usedBasis:
        fA213 = 4*cos(2*x*pi)*cos(6*z*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*cos(6*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA213*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB213 = 4*cos(2*y*pi)*sin(6*z*pi)*(2*cos(2*x*pi)**2 - 1) - 4*cos(2*x*pi)*sin(6*z*pi)*(2*cos(2*y*pi)**2 - 1)
        FB += SF.ai[idx_a]*fB213*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,3])
        idx_a += 1

    if 23 in usedBasis:
        fA105 = 4*cos(10*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA105*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB105 = 4*sin(10*z*pi)*(cos(2*x*pi) - cos(2*y*pi))
        FB += SF.ai[idx_a]*fB105*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,5])
        idx_a += 1

    if 24 in usedBasis:
        fA220 = 8*cos(4*x*pi)*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 25 in usedBasis:
        fA204 = 4*cos(8*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA204*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB204 = 4*sin(8*z*pi)*(cos(4*x*pi) - cos(4*y*pi))
        FB += SF.ai[idx_a]*fB204*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,4])
        idx_a += 1

    if 26 in usedBasis:
        fA221 = 8*cos(4*x*pi)*cos(4*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA221*Multi[idx_a]
        hkl.append([2,2,1])
        idx_a += 1

    if 27 in usedBasis:
        fA115 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(10*z*pi)
        FA += SF.ai[idx_a]*fA115*Multi[idx_a]
        hkl.append([1,1,5])
        idx_a += 1

    if 28 in usedBasis:
        fA300 = 4*cos(6*x*pi) + 4*cos(6*y*pi)
        FA += SF.ai[idx_a]*fA300*Multi[idx_a]
        hkl.append([3,0,0])
        idx_a += 1

    if 29 in usedBasis:
        fA222 = 8*cos(4*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA222*Multi[idx_a]
        hkl.append([2,2,2])
        idx_a += 1

    if 30 in usedBasis:
        fA214 = 4*cos(2*x*pi)*cos(8*z*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*cos(8*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA214*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB214 = 4*cos(2*y*pi)*sin(8*z*pi)*(2*cos(2*x*pi)**2 - 1) - 4*cos(2*x*pi)*sin(8*z*pi)*(2*cos(2*y*pi)**2 - 1)
        FB += SF.ai[idx_a]*fB214*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,4])
        idx_a += 1

    if 31 in usedBasis:
        fA006 = 8*cos(12*z*pi)
        FA += SF.ai[idx_a]*fA006*Multi[idx_a]
        hkl.append([0,0,6])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 1 1 1 1 0 1 0 1 1 0 1 0 0 0 0 1 0 
    # 115_2d0: [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0]
    return FA+FB, idx_theta, hkl
