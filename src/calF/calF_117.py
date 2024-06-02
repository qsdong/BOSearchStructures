# Generated at 2024-02-23 21:12:16
# Qingshu Dong

import numpy as np

def  calF_117(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([2, 4, 8, 4, 2, 8, 8, 16, 8, 4, 8, 8, 16, 2, 8, 16, 8, 8, 8, 8, 16, 16, 16, 4, 2, 8, 8, 16, 8, 4, 16, 8])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 117.0')

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
        fA110 = 8*cos(2*x*pi)*cos(2*y*pi)
        FA += SF.ai[idx_a]*fA110*Multi[idx_a]
        hkl.append([1,1,0])
        idx_a += 1

    if 2 in usedBasis:
        fA111 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA111*Multi[idx_a]
        hkl.append([1,1,1])
        idx_a += 1

    if 3 in usedBasis:
        fA200 = 4*cos(4*x*pi) + 4*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 4 in usedBasis:
        fA002 = 8*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA002*Multi[idx_a]
        hkl.append([0,0,2])
        idx_a += 1

    if 5 in usedBasis:
        fA210 = 4*sin(2*x*pi)*sin(4*y*pi) - 4*sin(4*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA210*Multi[idx_a]
        hkl.append([2,1,0])
        idx_a += 1

    if 6 in usedBasis:
        fA201 = 4*cos(2*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA201*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB201 = 4*sin(2*z*pi)*(cos(4*x*pi) - cos(4*y*pi))
        FB += SF.ai[idx_a]*fB201*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,1])
        idx_a += 1

    if 7 in usedBasis:
        fA211 = 4*cos(2*z*pi)*(sin(2*x*pi)*sin(4*y*pi) - sin(4*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = -4*sin(2*z*pi)*(sin(2*x*pi)*sin(4*y*pi) + sin(4*x*pi)*sin(2*y*pi))
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 8 in usedBasis:
        fA112 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA112*Multi[idx_a]
        hkl.append([1,1,2])
        idx_a += 1

    if 9 in usedBasis:
        fA220 = 8*cos(4*x*pi)*cos(4*y*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 10 in usedBasis:
        fA202 = 4*cos(4*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA202*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB202 = 4*sin(4*z*pi)*(cos(4*x*pi) - cos(4*y*pi))
        FB += SF.ai[idx_a]*fB202*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,2])
        idx_a += 1

    if 11 in usedBasis:
        fA221 = 8*cos(4*x*pi)*cos(4*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA221*Multi[idx_a]
        hkl.append([2,2,1])
        idx_a += 1

    if 12 in usedBasis:
        fA212 = 4*cos(4*z*pi)*(sin(2*x*pi)*sin(4*y*pi) - sin(4*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA212*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB212 = -4*sin(4*z*pi)*(sin(2*x*pi)*sin(4*y*pi) + sin(4*x*pi)*sin(2*y*pi))
        FB += SF.ai[idx_a]*fB212*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,2])
        idx_a += 1

    if 13 in usedBasis:
        fA003 = 8*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA003*Multi[idx_a]
        hkl.append([0,0,3])
        idx_a += 1

    if 14 in usedBasis:
        fA310 = 8*cos(2*x*pi)*cos(2*y*pi)*(2*cos(2*x*pi)**2 + 2*cos(2*y*pi)**2 - 3)
        FA += SF.ai[idx_a]*fA310*Multi[idx_a]
        hkl.append([3,1,0])
        idx_a += 1

    if 15 in usedBasis:
        fA311 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(2*z*pi)*(2*cos(2*x*pi)**2 + 2*cos(2*y*pi)**2 - 3)
        FA += SF.ai[idx_a]*fA311*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB311 = 16*cos(2*x*pi)*cos(2*y*pi)*sin(2*z*pi)*(cos(2*x*pi)**2 - cos(2*y*pi)**2)
        FB += SF.ai[idx_a]*fB311*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,1])
        idx_a += 1

    if 16 in usedBasis:
        fA113 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA113*Multi[idx_a]
        hkl.append([1,1,3])
        idx_a += 1

    if 17 in usedBasis:
        fA222 = 8*cos(4*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA222*Multi[idx_a]
        hkl.append([2,2,2])
        idx_a += 1

    if 18 in usedBasis:
        fA320 = 4*sin(4*x*pi)*sin(6*y*pi) - 4*sin(6*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA320*Multi[idx_a]
        hkl.append([3,2,0])
        idx_a += 1

    if 19 in usedBasis:
        fA203 = 4*cos(6*z*pi)*(cos(4*x*pi) + cos(4*y*pi))
        FA += SF.ai[idx_a]*fA203*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB203 = 4*sin(6*z*pi)*(cos(4*x*pi) - cos(4*y*pi))
        FB += SF.ai[idx_a]*fB203*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,3])
        idx_a += 1

    if 20 in usedBasis:
        fA321 = 4*cos(2*z*pi)*(sin(4*x*pi)*sin(6*y*pi) - sin(6*x*pi)*sin(4*y*pi))
        FA += SF.ai[idx_a]*fA321*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB321 = -4*sin(2*z*pi)*(sin(4*x*pi)*sin(6*y*pi) + sin(6*x*pi)*sin(4*y*pi))
        FB += SF.ai[idx_a]*fB321*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,1])
        idx_a += 1

    if 21 in usedBasis:
        fA312 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(4*z*pi)*(2*cos(2*x*pi)**2 + 2*cos(2*y*pi)**2 - 3)
        FA += SF.ai[idx_a]*fA312*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB312 = 16*cos(2*x*pi)*cos(2*y*pi)*sin(4*z*pi)*(cos(2*x*pi)**2 - cos(2*y*pi)**2)
        FB += SF.ai[idx_a]*fB312*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,2])
        idx_a += 1

    if 22 in usedBasis:
        fA213 = 4*cos(6*z*pi)*(sin(2*x*pi)*sin(4*y*pi) - sin(4*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA213*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB213 = -4*sin(6*z*pi)*(sin(2*x*pi)*sin(4*y*pi) + sin(4*x*pi)*sin(2*y*pi))
        FB += SF.ai[idx_a]*fB213*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,3])
        idx_a += 1

    if 23 in usedBasis:
        fA400 = 4*cos(8*x*pi) + 4*cos(8*y*pi)
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 24 in usedBasis:
        fA004 = 8*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA004*Multi[idx_a]
        hkl.append([0,0,4])
        idx_a += 1

    if 25 in usedBasis:
        fA410 = 4*sin(2*x*pi)*sin(8*y*pi) - 4*sin(8*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA410*Multi[idx_a]
        hkl.append([4,1,0])
        idx_a += 1

    if 26 in usedBasis:
        fA401 = 4*cos(2*z*pi)*(cos(8*x*pi) + cos(8*y*pi))
        FA += SF.ai[idx_a]*fA401*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB401 = 4*sin(2*z*pi)*(cos(8*x*pi) - cos(8*y*pi))
        FB += SF.ai[idx_a]*fB401*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,0,1])
        idx_a += 1

    if 27 in usedBasis:
        fA322 = 4*cos(4*z*pi)*(sin(4*x*pi)*sin(6*y*pi) - sin(6*x*pi)*sin(4*y*pi))
        FA += SF.ai[idx_a]*fA322*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB322 = -4*sin(4*z*pi)*(sin(4*x*pi)*sin(6*y*pi) + sin(6*x*pi)*sin(4*y*pi))
        FB += SF.ai[idx_a]*fB322*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,2])
        idx_a += 1

    if 28 in usedBasis:
        fA223 = 8*cos(4*x*pi)*cos(4*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA223*Multi[idx_a]
        hkl.append([2,2,3])
        idx_a += 1

    if 29 in usedBasis:
        fA330 = 8*cos(6*x*pi)*cos(6*y*pi)
        FA += SF.ai[idx_a]*fA330*Multi[idx_a]
        hkl.append([3,3,0])
        idx_a += 1

    if 30 in usedBasis:
        fA411 = 4*cos(2*z*pi)*(sin(2*x*pi)*sin(8*y*pi) - sin(8*x*pi)*sin(2*y*pi))
        FA += SF.ai[idx_a]*fA411*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB411 = -4*sin(2*z*pi)*(sin(2*x*pi)*sin(8*y*pi) + sin(8*x*pi)*sin(2*y*pi))
        FB += SF.ai[idx_a]*fB411*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,1,1])
        idx_a += 1

    if 31 in usedBasis:
        fA114 = 8*cos(2*x*pi)*cos(2*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA114*Multi[idx_a]
        hkl.append([1,1,4])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 0 0 0 0 1 1 0 0 1 0 1 0 0 1 0 0 0 1 1 1 1 0 0 0 1 1 0 0 1 0 
    # 117: [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0]
    return FA+FB, idx_theta, hkl
