# Generated at 2023-12-16 13:31:59
# Qingshu Dong

import numpy as np

def  calF_196(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([8, 6, 12, 24, 8, 6, 24, 24, 24, 8, 24, 12, 48, 24, 6, 24, 24, 24, 8, 24, 24, 24, 48, 24, 48, 6, 24, 24, 24, 12, 24, 8])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 196.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA111 = 48*cos(2*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA111*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB111 = -48*sin(2*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB111*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,1])
        idx_a += 1

    if 1 in usedBasis:
        fA200 = 16*cos(4*x*pi) + 16*cos(4*y*pi) + 16*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 2 in usedBasis:
        fA220 = 16*cos(4*x*pi)*cos(4*y*pi) + 16*cos(4*x*pi)*cos(4*z*pi) + 16*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 3 in usedBasis:
        fA311 = 16*cos(2*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 16*cos(2*x*pi)*cos(6*y*pi)*cos(2*z*pi) + 16*cos(6*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA311*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB311 = - 16*sin(2*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 16*sin(2*x*pi)*sin(6*y*pi)*sin(2*z*pi) - 16*sin(6*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB311*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,1])
        idx_a += 1

    if 4 in usedBasis:
        fA222 = 48*cos(4*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA222*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB222 = -48*sin(4*x*pi)*sin(4*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB222*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,2])
        idx_a += 1

    if 5 in usedBasis:
        fA400 = 16*cos(8*x*pi) + 16*cos(8*y*pi) + 16*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 6 in usedBasis:
        fA331 = 16*cos(2*x*pi)*cos(6*y*pi)*cos(6*z*pi) + 16*cos(6*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 16*cos(6*x*pi)*cos(6*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA331*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB331 = - 16*sin(2*x*pi)*sin(6*y*pi)*sin(6*z*pi) - 16*sin(6*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 16*sin(6*x*pi)*sin(6*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB331*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,3,1])
        idx_a += 1

    if 7 in usedBasis:
        fA420 = 16*cos(4*y*pi)*(2*cos(4*x*pi)**2 - 1) + 16*cos(4*x*pi)*(2*cos(4*z*pi)**2 - 1) + 16*cos(4*z*pi)*(2*cos(4*y*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA420*Multi[idx_a]
        hkl.append([4,2,0])
        idx_a += 1

    if 8 in usedBasis:
        fA422 = 16*cos(4*x*pi)*cos(4*y*pi)*(2*cos(4*z*pi)**2 - 1) + 16*cos(4*x*pi)*cos(4*z*pi)*(2*cos(4*y*pi)**2 - 1) + 16*cos(4*y*pi)*cos(4*z*pi)*(2*cos(4*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA422*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB422 = - 16*sin(4*x*pi)*sin(4*y*pi)*sin(8*z*pi) - 16*sin(4*x*pi)*sin(8*y*pi)*sin(4*z*pi) - 16*sin(8*x*pi)*sin(4*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB422*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,2,2])
        idx_a += 1

    if 9 in usedBasis:
        fA333 = 48*cos(6*x*pi)*cos(6*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA333*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB333 = -48*sin(6*x*pi)*sin(6*y*pi)*sin(6*z*pi)
        FB += SF.ai[idx_a]*fB333*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,3,3])
        idx_a += 1

    if 10 in usedBasis:
        fA511 = 16*cos(2*x*pi)*cos(2*y*pi)*cos(10*z*pi) + 16*cos(2*x*pi)*cos(10*y*pi)*cos(2*z*pi) + 16*cos(10*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA511*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB511 = - 16*sin(2*x*pi)*sin(2*y*pi)*sin(10*z*pi) - 16*sin(2*x*pi)*sin(10*y*pi)*sin(2*z*pi) - 16*sin(10*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB511*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,1,1])
        idx_a += 1

    if 11 in usedBasis:
        fA440 = 16*cos(8*x*pi)*cos(8*y*pi) + 16*cos(8*x*pi)*cos(8*z*pi) + 16*cos(8*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA440*Multi[idx_a]
        hkl.append([4,4,0])
        idx_a += 1

    if 12 in usedBasis:
        fA531 = 16*cos(2*x*pi)*cos(10*y*pi)*cos(6*z*pi) + 16*cos(6*x*pi)*cos(2*y*pi)*cos(10*z*pi) + 16*cos(10*x*pi)*cos(6*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA531*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB531 = - 16*sin(2*x*pi)*sin(10*y*pi)*sin(6*z*pi) - 16*sin(6*x*pi)*sin(2*y*pi)*sin(10*z*pi) - 16*sin(10*x*pi)*sin(6*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB531*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,3,1])
        idx_a += 1

    if 13 in usedBasis:
        fA442 = 16*cos(4*x*pi)*(2*cos(4*y*pi)**2 - 1)*(2*cos(4*z*pi)**2 - 1) + 16*cos(4*y*pi)*(2*cos(4*x*pi)**2 - 1)*(2*cos(4*z*pi)**2 - 1) + 16*cos(4*z*pi)*(2*cos(4*x*pi)**2 - 1)*(2*cos(4*y*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA442*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB442 = - 16*sin(4*x*pi)*sin(8*y*pi)*sin(8*z*pi) - 16*sin(8*x*pi)*sin(4*y*pi)*sin(8*z*pi) - 16*sin(8*x*pi)*sin(8*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB442*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,4,2])
        idx_a += 1

    if 14 in usedBasis:
        fA600 = 16*cos(12*x*pi) + 16*cos(12*y*pi) + 16*cos(12*z*pi)
        FA += SF.ai[idx_a]*fA600*Multi[idx_a]
        hkl.append([6,0,0])
        idx_a += 1

    if 15 in usedBasis:
        fA620 = 16*cos(12*x*pi)*cos(4*y*pi) + 16*cos(4*x*pi)*cos(12*z*pi) + 16*cos(12*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA620*Multi[idx_a]
        hkl.append([6,2,0])
        idx_a += 1

    if 16 in usedBasis:
        fA533 = 16*cos(6*x*pi)*cos(6*y*pi)*cos(10*z*pi) + 16*cos(6*x*pi)*cos(10*y*pi)*cos(6*z*pi) + 16*cos(10*x*pi)*cos(6*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA533*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB533 = - 16*sin(6*x*pi)*sin(6*y*pi)*sin(10*z*pi) - 16*sin(6*x*pi)*sin(10*y*pi)*sin(6*z*pi) - 16*sin(10*x*pi)*sin(6*y*pi)*sin(6*z*pi)
        FB += SF.ai[idx_a]*fB533*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,3,3])
        idx_a += 1

    if 17 in usedBasis:
        fA622 = 16*cos(4*x*pi)*cos(4*y*pi)*cos(12*z*pi) + 16*cos(4*x*pi)*cos(12*y*pi)*cos(4*z*pi) + 16*cos(12*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA622*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB622 = - 16*sin(4*x*pi)*sin(4*y*pi)*sin(12*z*pi) - 16*sin(4*x*pi)*sin(12*y*pi)*sin(4*z*pi) - 16*sin(12*x*pi)*sin(4*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB622*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,2,2])
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
        fA551 = 16*cos(2*x*pi)*cos(10*y*pi)*cos(10*z*pi) + 16*cos(10*x*pi)*cos(2*y*pi)*cos(10*z*pi) + 16*cos(10*x*pi)*cos(10*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA551*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB551 = - 16*sin(2*x*pi)*sin(10*y*pi)*sin(10*z*pi) - 16*sin(10*x*pi)*sin(2*y*pi)*sin(10*z*pi) - 16*sin(10*x*pi)*sin(10*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB551*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,5,1])
        idx_a += 1

    if 20 in usedBasis:
        fA711 = 16*cos(2*x*pi)*cos(2*y*pi)*cos(14*z*pi) + 16*cos(2*x*pi)*cos(14*y*pi)*cos(2*z*pi) + 16*cos(14*x*pi)*cos(2*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA711*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB711 = - 16*sin(2*x*pi)*sin(2*y*pi)*sin(14*z*pi) - 16*sin(2*x*pi)*sin(14*y*pi)*sin(2*z*pi) - 16*sin(14*x*pi)*sin(2*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB711*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([7,1,1])
        idx_a += 1

    if 21 in usedBasis:
        fA640 = 16*cos(12*x*pi)*cos(8*y*pi) + 16*cos(8*x*pi)*cos(12*z*pi) + 16*cos(12*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA640*Multi[idx_a]
        hkl.append([6,4,0])
        idx_a += 1

    if 22 in usedBasis:
        fA642 = - 16*cos(4*z*pi)*(3*cos(4*x*pi) - 4*cos(4*x*pi)**3)*(2*cos(4*y*pi)**2 - 1) - 16*cos(4*x*pi)*(3*cos(4*y*pi) - 4*cos(4*y*pi)**3)*(2*cos(4*z*pi)**2 - 1) - 16*cos(4*y*pi)*(3*cos(4*z*pi) - 4*cos(4*z*pi)**3)*(2*cos(4*x*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA642*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB642 = - 16*sin(4*x*pi)*sin(12*y*pi)*sin(8*z*pi) - 16*sin(8*x*pi)*sin(4*y*pi)*sin(12*z*pi) - 16*sin(12*x*pi)*sin(8*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB642*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,4,2])
        idx_a += 1

    if 23 in usedBasis:
        fA553 = 16*cos(6*x*pi)*cos(10*y*pi)*cos(10*z*pi) + 16*cos(10*x*pi)*cos(6*y*pi)*cos(10*z*pi) + 16*cos(10*x*pi)*cos(10*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA553*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB553 = - 16*sin(6*x*pi)*sin(10*y*pi)*sin(10*z*pi) - 16*sin(10*x*pi)*sin(6*y*pi)*sin(10*z*pi) - 16*sin(10*x*pi)*sin(10*y*pi)*sin(6*z*pi)
        FB += SF.ai[idx_a]*fB553*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,5,3])
        idx_a += 1

    if 24 in usedBasis:
        fA731 = 16*cos(2*x*pi)*cos(14*y*pi)*cos(6*z*pi) + 16*cos(6*x*pi)*cos(2*y*pi)*cos(14*z*pi) + 16*cos(14*x*pi)*cos(6*y*pi)*cos(2*z*pi)
        FA += SF.ai[idx_a]*fA731*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB731 = - 16*sin(2*x*pi)*sin(14*y*pi)*sin(6*z*pi) - 16*sin(6*x*pi)*sin(2*y*pi)*sin(14*z*pi) - 16*sin(14*x*pi)*sin(6*y*pi)*sin(2*z*pi)
        FB += SF.ai[idx_a]*fB731*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([7,3,1])
        idx_a += 1

    if 25 in usedBasis:
        fA800 = 16*cos(16*x*pi) + 16*cos(16*y*pi) + 16*cos(16*z*pi)
        FA += SF.ai[idx_a]*fA800*Multi[idx_a]
        hkl.append([8,0,0])
        idx_a += 1

    if 26 in usedBasis:
        fA733 = 16*cos(6*x*pi)*cos(6*y*pi)*cos(14*z*pi) + 16*cos(6*x*pi)*cos(14*y*pi)*cos(6*z*pi) + 16*cos(14*x*pi)*cos(6*y*pi)*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA733*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB733 = - 16*sin(6*x*pi)*sin(6*y*pi)*sin(14*z*pi) - 16*sin(6*x*pi)*sin(14*y*pi)*sin(6*z*pi) - 16*sin(14*x*pi)*sin(6*y*pi)*sin(6*z*pi)
        FB += SF.ai[idx_a]*fB733*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([7,3,3])
        idx_a += 1

    if 27 in usedBasis:
        fA644 = 16*cos(8*x*pi)*cos(8*y*pi)*cos(12*z*pi) + 16*cos(8*x*pi)*cos(12*y*pi)*cos(8*z*pi) + 16*cos(12*x*pi)*cos(8*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA644*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB644 = - 16*sin(8*x*pi)*sin(8*y*pi)*sin(12*z*pi) - 16*sin(8*x*pi)*sin(12*y*pi)*sin(8*z*pi) - 16*sin(12*x*pi)*sin(8*y*pi)*sin(8*z*pi)
        FB += SF.ai[idx_a]*fB644*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([6,4,4])
        idx_a += 1

    if 28 in usedBasis:
        fA820 = 16*cos(16*x*pi)*cos(4*y*pi) + 16*cos(4*x*pi)*cos(16*z*pi) + 16*cos(16*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA820*Multi[idx_a]
        hkl.append([8,2,0])
        idx_a += 1

    if 29 in usedBasis:
        fA660 = 16*cos(12*x*pi)*cos(12*y*pi) + 16*cos(12*x*pi)*cos(12*z*pi) + 16*cos(12*y*pi)*cos(12*z*pi)
        FA += SF.ai[idx_a]*fA660*Multi[idx_a]
        hkl.append([6,6,0])
        idx_a += 1

    if 30 in usedBasis:
        fA822 = 16*cos(4*x*pi)*cos(4*y*pi)*cos(16*z*pi) + 16*cos(4*x*pi)*cos(16*y*pi)*cos(4*z*pi) + 16*cos(16*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA822*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB822 = - 16*sin(4*x*pi)*sin(4*y*pi)*sin(16*z*pi) - 16*sin(4*x*pi)*sin(16*y*pi)*sin(4*z*pi) - 16*sin(16*x*pi)*sin(4*y*pi)*sin(4*z*pi)
        FB += SF.ai[idx_a]*fB822*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([8,2,2])
        idx_a += 1

    if 31 in usedBasis:
        fA555 = 48*cos(10*x*pi)*cos(10*y*pi)*cos(10*z*pi)
        FA += SF.ai[idx_a]*fA555*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB555 = -48*sin(10*x*pi)*sin(10*y*pi)*sin(10*z*pi)
        FB += SF.ai[idx_a]*fB555*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,5,5])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 1 0 0 1 1 0 1 0 1 1 1 0 1 1 0 0 1 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 
    # 196: [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    return FA+FB, idx_theta, hkl
