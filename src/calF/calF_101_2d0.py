# Generated at 2024-02-26 11:09:57
# Qingshu Dong

import numpy as np

def  calF_101_2d0(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([4, 2, 4, 8, 8, 8, 4, 2, 8, 8, 8, 8, 16, 16, 8, 16, 4, 8, 8, 8, 4, 8, 16, 2, 8, 8, 8, 16, 8, 16, 8, 16])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 101.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA100 = 4*cos(2*x*pi) + 4*cos(2*y*pi)
        FA += SF.ai[idx_a]*fA100*Multi[idx_a]
        hkl.append([1,0,0])
        idx_a += 1

    if 1 in usedBasis:
        fA002 = 8*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA002*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB002 = 8*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB002*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,2])
        idx_a += 1

    if 2 in usedBasis:
        fA110 = 8*cos(2*x*pi)*cos(2*y*pi)
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 3 in usedBasis:
        fA102 = 4*cos(4*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA102*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB102 = 4*sin(4*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FB += SF.ai[idx_a]*fB102*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,2])
        idx_a += 1

    if 4 in usedBasis:
        fA111 = -8*cos(2*z*pi)*sin(2*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA111*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB111 = -8*sin(2*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB111*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,1])
        idx_a += 1

    if 5 in usedBasis:
        fA112 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA112*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB112 = 8*cos(2*x*pi)*cos(2*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB112*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,2])
        idx_a += 1

    if 6 in usedBasis:
        fA200 = 4*cos(4*x*pi) + 4*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 7 in usedBasis:
        fA004 = 8*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA004*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB004 = 8*sin(8*z*pi)
        FB += SF.ai[idx_a]*fB004*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,4])
        idx_a += 1

    if 8 in usedBasis:
        fA113 = -8*cos(6*z*pi)*sin(2*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA113*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB113 = -8*sin(2*x*pi)*sin(2*y*pi)*sin(6*z*pi)
        FB += SF.ai[idx_a]*fB113*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,3])
        idx_a += 1

    if 9 in usedBasis:
        fA210 = 4*cos(2*x*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA210*Multi[idx_a]
        hkl.append([2,1,0])
        idx_a += 1

    if 10 in usedBasis:
        fA202 = 4*cos(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA202*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB202 = 4*sin(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FB += SF.ai[idx_a]*fB202*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,2])
        idx_a += 1

    if 11 in usedBasis:
        fA104 = 4*cos(8*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA104*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB104 = 4*sin(8*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FB += SF.ai[idx_a]*fB104*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,4])
        idx_a += 1

    if 12 in usedBasis:
        fA211 = -4*cos(2*z*pi)*(sin(2*x*pi)*sin(4*y*pi) + sin(4*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = -4*sin(2*z*pi)*(sin(2*x*pi)*sin(4*y*pi) + sin(4*x*pi)*sin(2*y*pi))
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 13 in usedBasis:
        fA212 = 4*cos(2*x*pi)*cos(4*z*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*cos(4*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA212*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB212 = 4*cos(2*x*pi)*sin(4*z*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*sin(4*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FB += SF.ai[idx_a]*fB212*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,2])
        idx_a += 1

    if 14 in usedBasis:
        fA114 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA114*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB114 = 8*cos(2*x*pi)*cos(2*y*pi)*sin(8*z*pi)
        FB += SF.ai[idx_a]*fB114*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,4])
        idx_a += 1

    if 15 in usedBasis:
        fA213 = -4*cos(6*z*pi)*(sin(2*x*pi)*sin(4*y*pi) + sin(4*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA213*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB213 = -4*sin(6*z*pi)*(sin(2*x*pi)*sin(4*y*pi) + sin(4*x*pi)*sin(2*y*pi))
        FB += SF.ai[idx_a]*fB213*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,3])
        idx_a += 1

    if 16 in usedBasis:
        fA220 = 8*cos(4*x*pi)*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 17 in usedBasis:
        fA204 = 4*cos(8*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA204*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB204 = 4*sin(8*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FB += SF.ai[idx_a]*fB204*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,4])
        idx_a += 1

    if 18 in usedBasis:
        fA221 = -8*cos(2*z*pi)*sin(4*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA221*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB221 = -8*sin(4*x*pi)*sin(4*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB221*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,1])
        idx_a += 1

    if 19 in usedBasis:
        fA115 = -8*cos(10*z*pi)*sin(2*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA115*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB115 = -8*sin(2*x*pi)*sin(2*y*pi)*sin(10*z*pi)
        FB += SF.ai[idx_a]*fB115*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,5])
        idx_a += 1

    if 20 in usedBasis:
        fA300 = 4*cos(6*x*pi) + 4*cos(6*y*pi)
        FA += SF.ai[idx_a]*fA300*Multi[idx_a]
        hkl.append([3,0,0])
        idx_a += 1

    if 21 in usedBasis:
        fA222 = 8*cos(4*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA222*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB222 = 8*cos(4*x*pi)*cos(4*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB222*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,2])
        idx_a += 1

    if 22 in usedBasis:
        fA214 = 4*cos(2*x*pi)*cos(8*z*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*cos(8*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA214*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB214 = 4*cos(2*x*pi)*sin(8*z*pi)*(2*cos(2*y*pi)**2 - 1) + 4*cos(2*y*pi)*sin(8*z*pi)*(2*cos(2*x*pi)**2 - 1)
        FB += SF.ai[idx_a]*fB214*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,4])
        idx_a += 1

    if 23 in usedBasis:
        fA006 = 8*cos(12*z*pi)
        FA += SF.ai[idx_a]*fA006*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB006 = 8*sin(12*z*pi)
        FB += SF.ai[idx_a]*fB006*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([0,0,6])
        idx_a += 1

    if 24 in usedBasis:
        fA310 = 8*cos(2*x*pi)*cos(2*y*pi)*(2*cos(2*x*pi)**2 + 2*cos(2*y*pi)**2 - 3)
        FA += SF.ai[idx_a]*fA310*Multi[idx_a]
        hkl.append([3,1,0])
        idx_a += 1

    if 25 in usedBasis:
        fA302 = 4*cos(4*z*pi)*(cos(6*x*pi) + cos(6*y*pi))
        FA += SF.ai[idx_a]*fA302*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB302 = 4*sin(4*z*pi)*(cos(6*x*pi) + cos(6*y*pi))
        FB += SF.ai[idx_a]*fB302*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,2])
        idx_a += 1

    if 26 in usedBasis:
        fA106 = 4*cos(12*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FA += SF.ai[idx_a]*fA106*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB106 = 4*sin(12*z*pi)*(cos(2*x*pi) + cos(2*y*pi))
        FB += SF.ai[idx_a]*fB106*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,6])
        idx_a += 1

    if 27 in usedBasis:
        fA311 = -4*cos(2*z*pi)*(sin(2*x*pi)*sin(6*y*pi) + sin(6*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA311*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB311 = -4*sin(2*z*pi)*(sin(2*x*pi)*sin(6*y*pi) + sin(6*x*pi)*sin(2*y*pi))
        FB += SF.ai[idx_a]*fB311*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,1])
        idx_a += 1

    if 28 in usedBasis:
        fA223 = -8*cos(6*z*pi)*sin(4*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA223*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB223 = -8*sin(4*x*pi)*sin(4*y*pi)*sin(6*z*pi)
        FB += SF.ai[idx_a]*fB223*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,3])
        idx_a += 1

    if 29 in usedBasis:
        fA312 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(4*z*pi)*(2*cos(2*x*pi)**2 + 2*cos(2*y*pi)**2 - 3)
        FA += SF.ai[idx_a]*fA312*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB312 = 8*cos(2*x*pi)*cos(2*y*pi)*sin(4*z*pi)*(2*cos(2*x*pi)**2 + 2*cos(2*y*pi)**2 - 3)
        FB += SF.ai[idx_a]*fB312*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,2])
        idx_a += 1

    if 30 in usedBasis:
        fA116 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(12*z*pi)
        FA += SF.ai[idx_a]*fA116*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB116 = 8*cos(2*x*pi)*cos(2*y*pi)*sin(12*z*pi)
        FB += SF.ai[idx_a]*fB116*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,6])
        idx_a += 1

    if 31 in usedBasis:
        fA215 = -4*cos(10*z*pi)*(sin(2*x*pi)*sin(4*y*pi) + sin(4*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA215*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB215 = -4*sin(10*z*pi)*(sin(2*x*pi)*sin(4*y*pi) + sin(4*x*pi)*sin(2*y*pi))
        FB += SF.ai[idx_a]*fB215*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,5])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 1 0 1 1 1 0 1 1 0 1 1 1 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 1 
    # 101_2d0: [0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
    return FA+FB, idx_theta, hkl
