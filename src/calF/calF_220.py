# Generated at 2023-12-16 14:12:26
# Qingshu Dong

import numpy as np

def  calF_220(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([24, 12, 24, 48, 6, 24, 24, 24, 48, 24, 48, 12, 24, 48, 24, 24, 48, 48, 8, 48, 24, 24, 24, 24, 48, 48, 24, 48, 48, 6, 48, 24])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 220.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA211 = - 32*cos(2*x*pi)*cos(2*y*pi)*sin(2*x*pi)*sin(2*z*pi) - 32*cos(2*y*pi)*cos(2*z*pi)*sin(2*x*pi)*sin(2*y*pi) - 32*cos(2*x*pi)*cos(2*z*pi)*sin(2*y*pi)*sin(2*z*pi)
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = 16*cos(2*x*pi)*sin(2*z*pi)*(2*cos(2*y*pi)**2 - 1) + 16*cos(2*y*pi)*sin(2*x*pi)*(2*cos(2*z*pi)**2 - 1) + 16*cos(2*z*pi)*sin(2*y*pi)*(2*cos(2*x*pi)**2 - 1)
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 1 in usedBasis:
        fA220 = 16*cos(4*x*pi)*cos(4*y*pi) + 16*cos(4*x*pi)*cos(4*z*pi) + 16*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 2 in usedBasis:
        fB310 = 8*cos(2*y*pi)*sin(6*x*pi) + 8*cos(6*y*pi)*sin(2*x*pi) + 8*cos(2*x*pi)*sin(6*z*pi) + 8*cos(6*x*pi)*sin(2*z*pi) + 8*cos(2*z*pi)*sin(6*y*pi) + 8*cos(6*z*pi)*sin(2*y*pi)
        FB += SF.ai[idx_a]*fB310*Multi[idx_a]
        hkl.append([3,1,0])
        idx_a += 1

    if 3 in usedBasis:
        fA321 = 8*cos(6*x*pi)*sin(2*y*pi)*sin(4*z*pi) - 8*cos(2*x*pi)*sin(6*y*pi)*sin(4*z*pi) - 8*cos(2*y*pi)*sin(4*x*pi)*sin(6*z*pi) + 8*cos(6*y*pi)*sin(4*x*pi)*sin(2*z*pi) - 8*cos(2*z*pi)*sin(6*x*pi)*sin(4*y*pi) + 8*cos(6*z*pi)*sin(2*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA321*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB321 = 8*cos(4*x*pi)*cos(6*z*pi)*sin(2*y*pi) - 8*cos(4*x*pi)*cos(2*z*pi)*sin(6*y*pi) - 8*cos(2*x*pi)*cos(4*y*pi)*sin(6*z*pi) + 8*cos(6*x*pi)*cos(4*y*pi)*sin(2*z*pi) - 8*cos(2*y*pi)*cos(4*z*pi)*sin(6*x*pi) + 8*cos(6*y*pi)*cos(4*z*pi)*sin(2*x*pi)
        FB += SF.ai[idx_a]*fB321*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,1])
        idx_a += 1

    if 4 in usedBasis:
        fA400 = 16*cos(8*x*pi) + 16*cos(8*y*pi) + 16*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 5 in usedBasis:
        fA420 = 16*(cos(4*x*pi) - cos(4*y*pi))*(cos(4*x*pi) - cos(4*z*pi))*(cos(4*y*pi) - cos(4*z*pi))
        FA += SF.ai[idx_a]*fA420*Multi[idx_a]
        hkl.append([4,2,0])
        idx_a += 1

    if 6 in usedBasis:
        fA332 = - 16*cos(6*x*pi)*sin(6*y*pi)*sin(4*z*pi) - 16*cos(6*y*pi)*sin(4*x*pi)*sin(6*z*pi) - 16*cos(6*z*pi)*sin(6*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA332*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB332 = 16*cos(4*x*pi)*cos(6*z*pi)*sin(6*y*pi) + 16*cos(6*x*pi)*cos(4*y*pi)*sin(6*z*pi) + 16*cos(6*y*pi)*cos(4*z*pi)*sin(6*x*pi)
        FB += SF.ai[idx_a]*fB332*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,3,2])
        idx_a += 1

    if 7 in usedBasis:
        fA422 = 16*cos(4*x*pi)*cos(4*y*pi)*(2*cos(4*z*pi)**2 - 1) + 16*cos(4*x*pi)*cos(4*z*pi)*(2*cos(4*y*pi)**2 - 1) + 16*cos(4*y*pi)*cos(4*z*pi)*(2*cos(4*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA422*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB422 = - 16*sin(4*x*pi)*sin(4*y*pi)*sin(8*z*pi) - 16*sin(4*x*pi)*sin(8*y*pi)*sin(4*z*pi) - 16*sin(8*x*pi)*sin(4*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB422*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,2,2])
        idx_a += 1

    if 8 in usedBasis:
        fA431 = - 8*cos(2*x*pi)*sin(6*y*pi)*sin(8*z*pi) - 8*cos(6*x*pi)*sin(2*y*pi)*sin(8*z*pi) - 8*cos(2*y*pi)*sin(8*x*pi)*sin(6*z*pi) - 8*cos(6*y*pi)*sin(8*x*pi)*sin(2*z*pi) - 8*cos(2*z*pi)*sin(6*x*pi)*sin(8*y*pi) - 8*cos(6*z*pi)*sin(2*x*pi)*sin(8*y*pi)
        FA += SF.ai[idx_a]*fA431*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB431 = 8*cos(2*x*pi)*cos(8*y*pi)*sin(6*z*pi) + 8*cos(6*x*pi)*cos(8*y*pi)*sin(2*z*pi) + 8*cos(8*x*pi)*cos(2*z*pi)*sin(6*y*pi) + 8*cos(8*x*pi)*cos(6*z*pi)*sin(2*y*pi) + 8*cos(2*y*pi)*cos(8*z*pi)*sin(6*x*pi) + 8*cos(6*y*pi)*cos(8*z*pi)*sin(2*x*pi)
        FB += SF.ai[idx_a]*fB431*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,3,1])
        idx_a += 1

    if 9 in usedBasis:
        fB510 = 8*cos(2*y*pi)*sin(10*x*pi) - 8*cos(10*y*pi)*sin(2*x*pi) + 8*cos(2*x*pi)*sin(10*z*pi) - 8*cos(10*x*pi)*sin(2*z*pi) + 8*cos(2*z*pi)*sin(10*y*pi) - 8*cos(10*z*pi)*sin(2*y*pi)
        FB += SF.ai[idx_a]*fB510*Multi[idx_a]
        hkl.append([5,1,0])
        idx_a += 1

    if 10 in usedBasis:
        fA521 = - 8*cos(2*x*pi)*sin(10*y*pi)*sin(4*z*pi) - 8*cos(10*x*pi)*sin(2*y*pi)*sin(4*z*pi) - 8*cos(2*y*pi)*sin(4*x*pi)*sin(10*z*pi) - 8*cos(10*y*pi)*sin(4*x*pi)*sin(2*z*pi) - 8*cos(2*z*pi)*sin(10*x*pi)*sin(4*y*pi) - 8*cos(10*z*pi)*sin(2*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA521*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB521 = 8*cos(2*x*pi)*cos(4*y*pi)*sin(10*z*pi) + 8*cos(4*x*pi)*cos(2*z*pi)*sin(10*y*pi) + 8*cos(4*x*pi)*cos(10*z*pi)*sin(2*y*pi) + 8*cos(10*x*pi)*cos(4*y*pi)*sin(2*z*pi) + 8*cos(2*y*pi)*cos(4*z*pi)*sin(10*x*pi) + 8*cos(10*y*pi)*cos(4*z*pi)*sin(2*x*pi)
        FB += SF.ai[idx_a]*fB521*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,2,1])
        idx_a += 1

    if 11 in usedBasis:
        fA440 = 16*cos(8*x*pi)*cos(8*y*pi) + 16*cos(8*x*pi)*cos(8*z*pi) + 16*cos(8*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA440*Multi[idx_a]
        hkl.append([4,4,0])
        idx_a += 1

    if 12 in usedBasis:
        fB530 = 8*cos(6*y*pi)*sin(10*x*pi) + 8*cos(10*y*pi)*sin(6*x*pi) + 8*cos(6*x*pi)*sin(10*z*pi) + 8*cos(10*x*pi)*sin(6*z*pi) + 8*cos(6*z*pi)*sin(10*y*pi) + 8*cos(10*z*pi)*sin(6*y*pi)
        FB += SF.ai[idx_a]*fB530*Multi[idx_a]
        hkl.append([5,3,0])
        idx_a += 1

    if 13 in usedBasis:
        fA532 = 8*cos(6*x*pi)*sin(10*y*pi)*sin(4*z*pi) - 8*cos(10*x*pi)*sin(6*y*pi)*sin(4*z*pi) + 8*cos(6*y*pi)*sin(4*x*pi)*sin(10*z*pi) - 8*cos(10*y*pi)*sin(4*x*pi)*sin(6*z*pi) + 8*cos(6*z*pi)*sin(10*x*pi)*sin(4*y*pi) - 8*cos(10*z*pi)*sin(6*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA532*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB532 = 8*cos(4*x*pi)*cos(6*z*pi)*sin(10*y*pi) - 8*cos(4*x*pi)*cos(10*z*pi)*sin(6*y*pi) + 8*cos(6*x*pi)*cos(4*y*pi)*sin(10*z*pi) - 8*cos(10*x*pi)*cos(4*y*pi)*sin(6*z*pi) + 8*cos(6*y*pi)*cos(4*z*pi)*sin(10*x*pi) - 8*cos(10*y*pi)*cos(4*z*pi)*sin(6*x*pi)
        FB += SF.ai[idx_a]*fB532*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,3,2])
        idx_a += 1

    if 14 in usedBasis:
        fA611 = - 16*cos(2*x*pi)*sin(2*y*pi)*sin(12*z*pi) - 16*cos(2*y*pi)*sin(12*x*pi)*sin(2*z*pi) - 16*cos(2*z*pi)*sin(2*x*pi)*sin(12*y*pi)
        FA += SF.ai[idx_a]*fA611*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB611 = 16*cos(2*x*pi)*cos(12*y*pi)*sin(2*z*pi) + 16*cos(12*x*pi)*cos(2*z*pi)*sin(2*y*pi) + 16*cos(2*y*pi)*cos(12*z*pi)*sin(2*x*pi)
        FB += SF.ai[idx_a]*fB611*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,1,1])
        idx_a += 1

    if 15 in usedBasis:
        fA620 = 8*cos(4*x*pi)*cos(12*y*pi) + 8*cos(12*x*pi)*cos(4*y*pi) + 8*cos(4*x*pi)*cos(12*z*pi) + 8*cos(12*x*pi)*cos(4*z*pi) + 8*cos(4*y*pi)*cos(12*z*pi) + 8*cos(12*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA620*Multi[idx_a]
        hkl.append([6,2,0])
        idx_a += 1

    if 16 in usedBasis:
        fA541 = 8*cos(10*x*pi)*sin(2*y*pi)*sin(8*z*pi) - 8*cos(2*x*pi)*sin(10*y*pi)*sin(8*z*pi) - 8*cos(2*y*pi)*sin(8*x*pi)*sin(10*z*pi) + 8*cos(10*y*pi)*sin(8*x*pi)*sin(2*z*pi) - 8*cos(2*z*pi)*sin(10*x*pi)*sin(8*y*pi) + 8*cos(10*z*pi)*sin(2*x*pi)*sin(8*y*pi)
        FA += SF.ai[idx_a]*fA541*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB541 = 8*cos(8*x*pi)*cos(10*z*pi)*sin(2*y*pi) - 8*cos(8*x*pi)*cos(2*z*pi)*sin(10*y*pi) - 8*cos(2*x*pi)*cos(8*y*pi)*sin(10*z*pi) + 8*cos(10*x*pi)*cos(8*y*pi)*sin(2*z*pi) - 8*cos(2*y*pi)*cos(8*z*pi)*sin(10*x*pi) + 8*cos(10*y*pi)*cos(8*z*pi)*sin(2*x*pi)
        FB += SF.ai[idx_a]*fB541*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,4,1])
        idx_a += 1

    if 17 in usedBasis:
        fA631 = 8*cos(2*x*pi)*sin(6*y*pi)*sin(12*z*pi) - 8*cos(6*x*pi)*sin(2*y*pi)*sin(12*z*pi) + 8*cos(2*y*pi)*sin(12*x*pi)*sin(6*z*pi) - 8*cos(6*y*pi)*sin(12*x*pi)*sin(2*z*pi) + 8*cos(2*z*pi)*sin(6*x*pi)*sin(12*y*pi) - 8*cos(6*z*pi)*sin(2*x*pi)*sin(12*y*pi)
        FA += SF.ai[idx_a]*fA631*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB631 = 8*cos(2*x*pi)*cos(12*y*pi)*sin(6*z*pi) - 8*cos(6*x*pi)*cos(12*y*pi)*sin(2*z*pi) + 8*cos(12*x*pi)*cos(2*z*pi)*sin(6*y*pi) - 8*cos(12*x*pi)*cos(6*z*pi)*sin(2*y*pi) + 8*cos(2*y*pi)*cos(12*z*pi)*sin(6*x*pi) - 8*cos(6*y*pi)*cos(12*z*pi)*sin(2*x*pi)
        FB += SF.ai[idx_a]*fB631*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,3,1])
        idx_a += 1

    if 18 in usedBasis:
        fA444 = 48*cos(8*x*pi)*cos(8*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA444*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB444 = -48*sin(8*x*pi)*sin(8*y*pi)*sin(8*z*pi)
        FB += SF.ai[idx_a]*fB444*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,4,4])
        idx_a += 1

    if 19 in usedBasis:
        fA543 = - 8*cos(6*x*pi)*sin(10*y*pi)*sin(8*z*pi) - 8*cos(10*x*pi)*sin(6*y*pi)*sin(8*z*pi) - 8*cos(6*y*pi)*sin(8*x*pi)*sin(10*z*pi) - 8*cos(10*y*pi)*sin(8*x*pi)*sin(6*z*pi) - 8*cos(6*z*pi)*sin(10*x*pi)*sin(8*y*pi) - 8*cos(10*z*pi)*sin(6*x*pi)*sin(8*y*pi)
        FA += SF.ai[idx_a]*fA543*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB543 = 8*cos(6*x*pi)*cos(8*y*pi)*sin(10*z*pi) + 8*cos(8*x*pi)*cos(6*z*pi)*sin(10*y*pi) + 8*cos(8*x*pi)*cos(10*z*pi)*sin(6*y*pi) + 8*cos(10*x*pi)*cos(8*y*pi)*sin(6*z*pi) + 8*cos(6*y*pi)*cos(8*z*pi)*sin(10*x*pi) + 8*cos(10*y*pi)*cos(8*z*pi)*sin(6*x*pi)
        FB += SF.ai[idx_a]*fB543*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,4,3])
        idx_a += 1

    if 20 in usedBasis:
        fB710 = 8*cos(2*y*pi)*sin(14*x*pi) + 8*cos(14*y*pi)*sin(2*x*pi) + 8*cos(2*x*pi)*sin(14*z*pi) + 8*cos(14*x*pi)*sin(2*z*pi) + 8*cos(2*z*pi)*sin(14*y*pi) + 8*cos(14*z*pi)*sin(2*y*pi)
        FB += SF.ai[idx_a]*fB710*Multi[idx_a]
        hkl.append([7,1,0])
        idx_a += 1

    if 21 in usedBasis:
        fA640 = 8*cos(12*x*pi)*cos(8*y*pi) - 8*cos(8*x*pi)*cos(12*y*pi) + 8*cos(8*x*pi)*cos(12*z*pi) - 8*cos(12*x*pi)*cos(8*z*pi) - 8*cos(8*y*pi)*cos(12*z*pi) + 8*cos(12*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA640*Multi[idx_a]
        hkl.append([6,4,0])
        idx_a += 1

    if 22 in usedBasis:
        fA552 = - 16*cos(10*x*pi)*sin(10*y*pi)*sin(4*z*pi) - 16*cos(10*y*pi)*sin(4*x*pi)*sin(10*z*pi) - 16*cos(10*z*pi)*sin(10*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA552*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB552 = 16*cos(4*x*pi)*cos(10*z*pi)*sin(10*y*pi) + 16*cos(10*x*pi)*cos(4*y*pi)*sin(10*z*pi) + 16*cos(10*y*pi)*cos(4*z*pi)*sin(10*x*pi)
        FB += SF.ai[idx_a]*fB552*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,5,2])
        idx_a += 1

    if 23 in usedBasis:
        fA633 = - 32*cos(6*x*pi)*cos(6*y*pi)*sin(6*x*pi)*sin(6*z*pi) - 32*cos(6*y*pi)*cos(6*z*pi)*sin(6*x*pi)*sin(6*y*pi) - 32*cos(6*x*pi)*cos(6*z*pi)*sin(6*y*pi)*sin(6*z*pi)
        FA += SF.ai[idx_a]*fA633*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB633 = 16*cos(6*x*pi)*sin(6*z*pi)*(2*cos(6*y*pi)**2 - 1) + 16*cos(6*y*pi)*sin(6*x*pi)*(2*cos(6*z*pi)**2 - 1) + 16*cos(6*z*pi)*sin(6*y*pi)*(2*cos(6*x*pi)**2 - 1)
        FB += SF.ai[idx_a]*fB633*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,3,3])
        idx_a += 1

    if 24 in usedBasis:
        fA721 = 8*cos(14*x*pi)*sin(2*y*pi)*sin(4*z*pi) - 8*cos(2*x*pi)*sin(14*y*pi)*sin(4*z*pi) - 8*cos(2*y*pi)*sin(4*x*pi)*sin(14*z*pi) + 8*cos(14*y*pi)*sin(4*x*pi)*sin(2*z*pi) - 8*cos(2*z*pi)*sin(14*x*pi)*sin(4*y*pi) + 8*cos(14*z*pi)*sin(2*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA721*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB721 = 8*cos(4*x*pi)*cos(14*z*pi)*sin(2*y*pi) - 8*cos(4*x*pi)*cos(2*z*pi)*sin(14*y*pi) - 8*cos(2*x*pi)*cos(4*y*pi)*sin(14*z*pi) + 8*cos(14*x*pi)*cos(4*y*pi)*sin(2*z*pi) - 8*cos(2*y*pi)*cos(4*z*pi)*sin(14*x*pi) + 8*cos(14*y*pi)*cos(4*z*pi)*sin(2*x*pi)
        FB += SF.ai[idx_a]*fB721*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([7,2,1])
        idx_a += 1

    if 25 in usedBasis:
        fA642 = 8*cos(4*x*pi)*cos(8*y*pi)*cos(12*z*pi) + 8*cos(4*x*pi)*cos(12*y*pi)*cos(8*z*pi) + 8*cos(8*x*pi)*cos(4*y*pi)*cos(12*z*pi) + 8*cos(8*x*pi)*cos(12*y*pi)*cos(4*z*pi) + 8*cos(12*x*pi)*cos(4*y*pi)*cos(8*z*pi) + 8*cos(12*x*pi)*cos(8*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA642*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB642 = - 8*sin(4*x*pi)*sin(8*y*pi)*sin(12*z*pi) - 8*sin(4*x*pi)*sin(12*y*pi)*sin(8*z*pi) - 8*sin(8*x*pi)*sin(4*y*pi)*sin(12*z*pi) - 8*sin(8*x*pi)*sin(12*y*pi)*sin(4*z*pi) - 8*sin(12*x*pi)*sin(4*y*pi)*sin(8*z*pi) - 8*sin(12*x*pi)*sin(8*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB642*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,4,2])
        idx_a += 1

    if 26 in usedBasis:
        fB730 = 8*cos(6*y*pi)*sin(14*x*pi) - 8*cos(14*y*pi)*sin(6*x*pi) + 8*cos(6*x*pi)*sin(14*z*pi) - 8*cos(14*x*pi)*sin(6*z*pi) + 8*cos(6*z*pi)*sin(14*y*pi) - 8*cos(14*z*pi)*sin(6*y*pi)
        FB += SF.ai[idx_a]*fB730*Multi[idx_a]
        hkl.append([7,3,0])
        idx_a += 1

    if 27 in usedBasis:
        fA651 = - 8*cos(2*x*pi)*sin(10*y*pi)*sin(12*z*pi) - 8*cos(10*x*pi)*sin(2*y*pi)*sin(12*z*pi) - 8*cos(2*y*pi)*sin(12*x*pi)*sin(10*z*pi) - 8*cos(10*y*pi)*sin(12*x*pi)*sin(2*z*pi) - 8*cos(2*z*pi)*sin(10*x*pi)*sin(12*y*pi) - 8*cos(10*z*pi)*sin(2*x*pi)*sin(12*y*pi)
        FA += SF.ai[idx_a]*fA651*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB651 = 8*cos(2*x*pi)*cos(12*y*pi)*sin(10*z*pi) + 8*cos(10*x*pi)*cos(12*y*pi)*sin(2*z*pi) + 8*cos(12*x*pi)*cos(2*z*pi)*sin(10*y*pi) + 8*cos(12*x*pi)*cos(10*z*pi)*sin(2*y*pi) + 8*cos(2*y*pi)*cos(12*z*pi)*sin(10*x*pi) + 8*cos(10*y*pi)*cos(12*z*pi)*sin(2*x*pi)
        FB += SF.ai[idx_a]*fB651*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,5,1])
        idx_a += 1

    if 28 in usedBasis:
        fA732 = - 8*cos(6*x*pi)*sin(14*y*pi)*sin(4*z*pi) - 8*cos(14*x*pi)*sin(6*y*pi)*sin(4*z*pi) - 8*cos(6*y*pi)*sin(4*x*pi)*sin(14*z*pi) - 8*cos(14*y*pi)*sin(4*x*pi)*sin(6*z*pi) - 8*cos(6*z*pi)*sin(14*x*pi)*sin(4*y*pi) - 8*cos(14*z*pi)*sin(6*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA732*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB732 = 8*cos(4*x*pi)*cos(6*z*pi)*sin(14*y*pi) + 8*cos(4*x*pi)*cos(14*z*pi)*sin(6*y*pi) + 8*cos(6*x*pi)*cos(4*y*pi)*sin(14*z*pi) + 8*cos(14*x*pi)*cos(4*y*pi)*sin(6*z*pi) + 8*cos(6*y*pi)*cos(4*z*pi)*sin(14*x*pi) + 8*cos(14*y*pi)*cos(4*z*pi)*sin(6*x*pi)
        FB += SF.ai[idx_a]*fB732*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([7,3,2])
        idx_a += 1

    if 29 in usedBasis:
        fA800 = 16*cos(16*x*pi) + 16*cos(16*y*pi) + 16*cos(16*z*pi)
        FA += SF.ai[idx_a]*fA800*Multi[idx_a]
        hkl.append([8,0,0])
        idx_a += 1

    if 30 in usedBasis:
        fA741 = - 8*cos(2*x*pi)*sin(14*y*pi)*sin(8*z*pi) - 8*cos(14*x*pi)*sin(2*y*pi)*sin(8*z*pi) - 8*cos(2*y*pi)*sin(8*x*pi)*sin(14*z*pi) - 8*cos(14*y*pi)*sin(8*x*pi)*sin(2*z*pi) - 8*cos(2*z*pi)*sin(14*x*pi)*sin(8*y*pi) - 8*cos(14*z*pi)*sin(2*x*pi)*sin(8*y*pi)
        FA += SF.ai[idx_a]*fA741*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB741 = 8*cos(2*x*pi)*cos(8*y*pi)*sin(14*z*pi) + 8*cos(8*x*pi)*cos(2*z*pi)*sin(14*y*pi) + 8*cos(8*x*pi)*cos(14*z*pi)*sin(2*y*pi) + 8*cos(14*x*pi)*cos(8*y*pi)*sin(2*z*pi) + 8*cos(2*y*pi)*cos(8*z*pi)*sin(14*x*pi) + 8*cos(14*y*pi)*cos(8*z*pi)*sin(2*x*pi)
        FB += SF.ai[idx_a]*fB741*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([7,4,1])
        idx_a += 1

    if 31 in usedBasis:
        fA820 = 8*cos(16*x*pi)*cos(4*y*pi) - 8*cos(4*x*pi)*cos(16*y*pi) + 8*cos(4*x*pi)*cos(16*z*pi) - 8*cos(16*x*pi)*cos(4*z*pi) - 8*cos(4*y*pi)*cos(16*z*pi) + 8*cos(16*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA820*Multi[idx_a]
        hkl.append([8,2,0])
        idx_a += 1

    # empty F record
    # 1 1 0 1 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 1 1 
    # 1 0 1 1 0 0 1 1 1 1 1 0 1 1 1 0 1 1 1 1 1 0 1 1 1 1 1 1 1 0 1 0 
    # 220: [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0]
    return FA+FB, idx_theta, hkl
