# Generated at 2023-12-16 15:13:31
# Qingshu Dong

import numpy as np

def  calF_227(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([8, 12, 24, 8, 6, 24, 24, 8, 24, 12, 48, 24, 24, 24, 24, 8, 24, 24, 48, 24, 48, 6, 24, 24, 12, 24, 8, 48, 24, 24, 48, 24])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 227.2')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA111 = - 96*cos(2*x*pi)*cos(2*y*pi)*cos(2*z*pi) - 96*cos(2*x*pi)*sin(2*y*pi)*sin(2*z*pi) - 96*cos(2*y*pi)*sin(2*x*pi)*sin(2*z*pi) - 96*cos(2*z*pi)*sin(2*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA111*Multi[idx_a]
        hkl.append([1,1,1])
        idx_a += 1

    if 1 in usedBasis:
        fA220 = - 64*sin(4*x*pi)*sin(4*y*pi) - 64*sin(4*x*pi)*sin(4*z*pi) - 64*sin(4*y*pi)*sin(4*z*pi)
        FA += SF.ai[idx_a]*fA220*Multi[idx_a]
        hkl.append([2,2,0])
        idx_a += 1

    if 2 in usedBasis:
        fA311 = 32*cos(2*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 32*cos(2*x*pi)*cos(6*y*pi)*cos(2*z*pi) + 32*cos(6*x*pi)*cos(2*y*pi)*cos(2*z*pi) - 32*cos(2*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 32*cos(2*x*pi)*sin(6*y*pi)*sin(2*z*pi) + 32*cos(6*x*pi)*sin(2*y*pi)*sin(2*z*pi) - 32*cos(2*y*pi)*sin(2*x*pi)*sin(6*z*pi) - 32*cos(2*y*pi)*sin(6*x*pi)*sin(2*z*pi) + 32*cos(6*y*pi)*sin(2*x*pi)*sin(2*z*pi) - 32*cos(2*z*pi)*sin(2*x*pi)*sin(6*y*pi) - 32*cos(2*z*pi)*sin(6*x*pi)*sin(2*y*pi) + 32*cos(6*z*pi)*sin(2*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA311*Multi[idx_a]
        hkl.append([3,1,1])
        idx_a += 1

    if 3 in usedBasis:
        fA222 = 192*cos(4*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA222*Multi[idx_a]
        hkl.append([2,2,2])
        idx_a += 1

    if 4 in usedBasis:
        fA400 = 64*cos(8*x*pi) + 64*cos(8*y*pi) + 64*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 5 in usedBasis:
        fA331 = 32*cos(2*x*pi)*cos(6*y*pi)*cos(6*z*pi) + 32*cos(6*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 32*cos(6*x*pi)*cos(6*y*pi)*cos(2*z*pi) + 32*cos(2*x*pi)*sin(6*y*pi)*sin(6*z*pi) - 32*cos(6*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 32*cos(6*x*pi)*sin(6*y*pi)*sin(2*z*pi) + 32*cos(2*y*pi)*sin(6*x*pi)*sin(6*z*pi) - 32*cos(6*y*pi)*sin(2*x*pi)*sin(6*z*pi) - 32*cos(6*y*pi)*sin(6*x*pi)*sin(2*z*pi) + 32*cos(2*z*pi)*sin(6*x*pi)*sin(6*y*pi) - 32*cos(6*z*pi)*sin(2*x*pi)*sin(6*y*pi) - 32*cos(6*z*pi)*sin(6*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA331*Multi[idx_a]
        hkl.append([3,3,1])
        idx_a += 1

    if 6 in usedBasis:
        fA422 = - 64*cos(8*x*pi)*sin(4*y*pi)*sin(4*z*pi) - 64*cos(8*y*pi)*sin(4*x*pi)*sin(4*z*pi) - 64*cos(8*z*pi)*sin(4*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA422*Multi[idx_a]
        hkl.append([4,2,2])
        idx_a += 1

    if 7 in usedBasis:
        fA333 = - 96*cos(6*x*pi)*cos(6*y*pi)*cos(6*z*pi) - 96*cos(6*x*pi)*sin(6*y*pi)*sin(6*z*pi) - 96*cos(6*y*pi)*sin(6*x*pi)*sin(6*z*pi) - 96*cos(6*z*pi)*sin(6*x*pi)*sin(6*y*pi)
        FA += SF.ai[idx_a]*fA333*Multi[idx_a]
        hkl.append([3,3,3])
        idx_a += 1

    if 8 in usedBasis:
        fA511 = - 32*cos(2*x*pi)*cos(2*y*pi)*cos(10*z*pi) - 32*cos(2*x*pi)*cos(10*y*pi)*cos(2*z*pi) - 32*cos(10*x*pi)*cos(2*y*pi)*cos(2*z*pi) - 32*cos(2*x*pi)*sin(2*y*pi)*sin(10*z*pi) - 32*cos(2*x*pi)*sin(10*y*pi)*sin(2*z*pi) - 32*cos(10*x*pi)*sin(2*y*pi)*sin(2*z*pi) - 32*cos(2*y*pi)*sin(2*x*pi)*sin(10*z*pi) - 32*cos(2*y*pi)*sin(10*x*pi)*sin(2*z*pi) - 32*cos(10*y*pi)*sin(2*x*pi)*sin(2*z*pi) - 32*cos(2*z*pi)*sin(2*x*pi)*sin(10*y*pi) - 32*cos(2*z*pi)*sin(10*x*pi)*sin(2*y*pi) - 32*cos(10*z*pi)*sin(2*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA511*Multi[idx_a]
        hkl.append([5,1,1])
        idx_a += 1

    if 9 in usedBasis:
        fA440 = 64*cos(8*x*pi)*cos(8*y*pi) + 64*cos(8*x*pi)*cos(8*z*pi) + 64*cos(8*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA440*Multi[idx_a]
        hkl.append([4,4,0])
        idx_a += 1

    if 10 in usedBasis:
        fA531 = 16*cos(2*x*pi)*cos(6*y*pi)*cos(10*z*pi) + 16*cos(2*x*pi)*cos(10*y*pi)*cos(6*z*pi) + 16*cos(6*x*pi)*cos(2*y*pi)*cos(10*z*pi) + 16*cos(6*x*pi)*cos(10*y*pi)*cos(2*z*pi) + 16*cos(10*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 16*cos(10*x*pi)*cos(6*y*pi)*cos(2*z*pi) - 16*cos(2*x*pi)*sin(6*y*pi)*sin(10*z*pi) - 16*cos(2*x*pi)*sin(10*y*pi)*sin(6*z*pi) + 16*cos(6*x*pi)*sin(2*y*pi)*sin(10*z*pi) + 16*cos(6*x*pi)*sin(10*y*pi)*sin(2*z*pi) - 16*cos(10*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 16*cos(10*x*pi)*sin(6*y*pi)*sin(2*z*pi) - 16*cos(2*y*pi)*sin(6*x*pi)*sin(10*z*pi) - 16*cos(2*y*pi)*sin(10*x*pi)*sin(6*z*pi) + 16*cos(6*y*pi)*sin(2*x*pi)*sin(10*z*pi) + 16*cos(6*y*pi)*sin(10*x*pi)*sin(2*z*pi) - 16*cos(10*y*pi)*sin(2*x*pi)*sin(6*z*pi) - 16*cos(10*y*pi)*sin(6*x*pi)*sin(2*z*pi) - 16*cos(2*z*pi)*sin(6*x*pi)*sin(10*y*pi) - 16*cos(2*z*pi)*sin(10*x*pi)*sin(6*y*pi) + 16*cos(6*z*pi)*sin(2*x*pi)*sin(10*y*pi) + 16*cos(6*z*pi)*sin(10*x*pi)*sin(2*y*pi) - 16*cos(10*z*pi)*sin(2*x*pi)*sin(6*y*pi) - 16*cos(10*z*pi)*sin(6*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA531*Multi[idx_a]
        hkl.append([5,3,1])
        idx_a += 1

    if 11 in usedBasis:
        fA442 = - 64*cos(4*x*pi)*sin(8*y*pi)*sin(8*z*pi) - 64*cos(4*y*pi)*sin(8*x*pi)*sin(8*z*pi) - 64*cos(4*z*pi)*sin(8*x*pi)*sin(8*y*pi)
        FA += SF.ai[idx_a]*fA442*Multi[idx_a]
        hkl.append([4,4,2])
        idx_a += 1

    if 12 in usedBasis:
        fA620 = - 32*sin(4*x*pi)*sin(12*y*pi) - 32*sin(12*x*pi)*sin(4*y*pi) - 32*sin(4*x*pi)*sin(12*z*pi) - 32*sin(12*x*pi)*sin(4*z*pi) - 32*sin(4*y*pi)*sin(12*z*pi) - 32*sin(12*y*pi)*sin(4*z*pi)
        FA += SF.ai[idx_a]*fA620*Multi[idx_a]
        hkl.append([6,2,0])
        idx_a += 1

    if 13 in usedBasis:
        fA533 = 32*cos(6*x*pi)*cos(6*y*pi)*cos(10*z*pi) + 32*cos(6*x*pi)*cos(10*y*pi)*cos(6*z*pi) + 32*cos(10*x*pi)*cos(6*y*pi)*cos(6*z*pi) - 32*cos(6*x*pi)*sin(6*y*pi)*sin(10*z*pi) - 32*cos(6*x*pi)*sin(10*y*pi)*sin(6*z*pi) + 32*cos(10*x*pi)*sin(6*y*pi)*sin(6*z*pi) - 32*cos(6*y*pi)*sin(6*x*pi)*sin(10*z*pi) - 32*cos(6*y*pi)*sin(10*x*pi)*sin(6*z*pi) + 32*cos(10*y*pi)*sin(6*x*pi)*sin(6*z*pi) - 32*cos(6*z*pi)*sin(6*x*pi)*sin(10*y*pi) - 32*cos(6*z*pi)*sin(10*x*pi)*sin(6*y*pi) + 32*cos(10*z*pi)*sin(6*x*pi)*sin(6*y*pi)
        FA += SF.ai[idx_a]*fA533*Multi[idx_a]
        hkl.append([5,3,3])
        idx_a += 1

    if 14 in usedBasis:
        fA622 = 64*cos(4*x*pi)*cos(4*y*pi)*cos(12*z*pi) + 64*cos(4*x*pi)*cos(12*y*pi)*cos(4*z*pi) + 64*cos(12*x*pi)*cos(4*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA622*Multi[idx_a]
        hkl.append([6,2,2])
        idx_a += 1

    if 15 in usedBasis:
        fA444 = 192*cos(8*x*pi)*cos(8*y*pi)*cos(8*z*pi)
        FA += SF.ai[idx_a]*fA444*Multi[idx_a]
        hkl.append([4,4,4])
        idx_a += 1

    if 16 in usedBasis:
        fA551 = - 32*cos(2*x*pi)*cos(10*y*pi)*cos(10*z*pi) - 32*cos(10*x*pi)*cos(2*y*pi)*cos(10*z*pi) - 32*cos(10*x*pi)*cos(10*y*pi)*cos(2*z*pi) - 32*cos(2*x*pi)*sin(10*y*pi)*sin(10*z*pi) - 32*cos(10*x*pi)*sin(2*y*pi)*sin(10*z*pi) - 32*cos(10*x*pi)*sin(10*y*pi)*sin(2*z*pi) - 32*cos(2*y*pi)*sin(10*x*pi)*sin(10*z*pi) - 32*cos(10*y*pi)*sin(2*x*pi)*sin(10*z*pi) - 32*cos(10*y*pi)*sin(10*x*pi)*sin(2*z*pi) - 32*cos(2*z*pi)*sin(10*x*pi)*sin(10*y*pi) - 32*cos(10*z*pi)*sin(2*x*pi)*sin(10*y*pi) - 32*cos(10*z*pi)*sin(10*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA551*Multi[idx_a]
        hkl.append([5,5,1])
        idx_a += 1

    if 17 in usedBasis:
        fA711 = 32*cos(2*x*pi)*cos(2*y*pi)*cos(14*z*pi) + 32*cos(2*x*pi)*cos(14*y*pi)*cos(2*z*pi) + 32*cos(14*x*pi)*cos(2*y*pi)*cos(2*z*pi) - 32*cos(2*x*pi)*sin(2*y*pi)*sin(14*z*pi) - 32*cos(2*x*pi)*sin(14*y*pi)*sin(2*z*pi) + 32*cos(14*x*pi)*sin(2*y*pi)*sin(2*z*pi) - 32*cos(2*y*pi)*sin(2*x*pi)*sin(14*z*pi) - 32*cos(2*y*pi)*sin(14*x*pi)*sin(2*z*pi) + 32*cos(14*y*pi)*sin(2*x*pi)*sin(2*z*pi) - 32*cos(2*z*pi)*sin(2*x*pi)*sin(14*y*pi) - 32*cos(2*z*pi)*sin(14*x*pi)*sin(2*y*pi) + 32*cos(14*z*pi)*sin(2*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA711*Multi[idx_a]
        hkl.append([7,1,1])
        idx_a += 1

    if 18 in usedBasis:
        fA642 = - 32*cos(8*x*pi)*sin(4*y*pi)*sin(12*z*pi) - 32*cos(8*x*pi)*sin(12*y*pi)*sin(4*z*pi) - 32*cos(8*y*pi)*sin(4*x*pi)*sin(12*z*pi) - 32*cos(8*y*pi)*sin(12*x*pi)*sin(4*z*pi) - 32*cos(8*z*pi)*sin(4*x*pi)*sin(12*y*pi) - 32*cos(8*z*pi)*sin(12*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA642*Multi[idx_a]
        hkl.append([6,4,2])
        idx_a += 1

    if 19 in usedBasis:
        fA553 = 32*cos(6*x*pi)*cos(10*y*pi)*cos(10*z*pi) + 32*cos(10*x*pi)*cos(6*y*pi)*cos(10*z*pi) + 32*cos(10*x*pi)*cos(10*y*pi)*cos(6*z*pi) + 32*cos(6*x*pi)*sin(10*y*pi)*sin(10*z*pi) - 32*cos(10*x*pi)*sin(6*y*pi)*sin(10*z*pi) - 32*cos(10*x*pi)*sin(10*y*pi)*sin(6*z*pi) + 32*cos(6*y*pi)*sin(10*x*pi)*sin(10*z*pi) - 32*cos(10*y*pi)*sin(6*x*pi)*sin(10*z*pi) - 32*cos(10*y*pi)*sin(10*x*pi)*sin(6*z*pi) + 32*cos(6*z*pi)*sin(10*x*pi)*sin(10*y*pi) - 32*cos(10*z*pi)*sin(6*x*pi)*sin(10*y*pi) - 32*cos(10*z*pi)*sin(10*x*pi)*sin(6*y*pi)
        FA += SF.ai[idx_a]*fA553*Multi[idx_a]
        hkl.append([5,5,3])
        idx_a += 1

    if 20 in usedBasis:
        fA731 = 16*cos(2*x*pi)*cos(6*y*pi)*cos(14*z*pi) + 16*cos(2*x*pi)*cos(14*y*pi)*cos(6*z*pi) + 16*cos(6*x*pi)*cos(2*y*pi)*cos(14*z*pi) + 16*cos(6*x*pi)*cos(14*y*pi)*cos(2*z*pi) + 16*cos(14*x*pi)*cos(2*y*pi)*cos(6*z*pi) + 16*cos(14*x*pi)*cos(6*y*pi)*cos(2*z*pi) + 16*cos(2*x*pi)*sin(6*y*pi)*sin(14*z*pi) + 16*cos(2*x*pi)*sin(14*y*pi)*sin(6*z*pi) - 16*cos(6*x*pi)*sin(2*y*pi)*sin(14*z*pi) - 16*cos(6*x*pi)*sin(14*y*pi)*sin(2*z*pi) - 16*cos(14*x*pi)*sin(2*y*pi)*sin(6*z*pi) - 16*cos(14*x*pi)*sin(6*y*pi)*sin(2*z*pi) + 16*cos(2*y*pi)*sin(6*x*pi)*sin(14*z*pi) + 16*cos(2*y*pi)*sin(14*x*pi)*sin(6*z*pi) - 16*cos(6*y*pi)*sin(2*x*pi)*sin(14*z*pi) - 16*cos(6*y*pi)*sin(14*x*pi)*sin(2*z*pi) - 16*cos(14*y*pi)*sin(2*x*pi)*sin(6*z*pi) - 16*cos(14*y*pi)*sin(6*x*pi)*sin(2*z*pi) + 16*cos(2*z*pi)*sin(6*x*pi)*sin(14*y*pi) + 16*cos(2*z*pi)*sin(14*x*pi)*sin(6*y*pi) - 16*cos(6*z*pi)*sin(2*x*pi)*sin(14*y*pi) - 16*cos(6*z*pi)*sin(14*x*pi)*sin(2*y*pi) - 16*cos(14*z*pi)*sin(2*x*pi)*sin(6*y*pi) - 16*cos(14*z*pi)*sin(6*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA731*Multi[idx_a]
        hkl.append([7,3,1])
        idx_a += 1

    if 21 in usedBasis:
        fA800 = 64*cos(16*x*pi) + 64*cos(16*y*pi) + 64*cos(16*z*pi)
        FA += SF.ai[idx_a]*fA800*Multi[idx_a]
        hkl.append([8,0,0])
        idx_a += 1

    if 22 in usedBasis:
        fA733 = - 32*cos(6*x*pi)*cos(6*y*pi)*cos(14*z*pi) - 32*cos(6*x*pi)*cos(14*y*pi)*cos(6*z*pi) - 32*cos(14*x*pi)*cos(6*y*pi)*cos(6*z*pi) - 32*cos(6*x*pi)*sin(6*y*pi)*sin(14*z*pi) - 32*cos(6*x*pi)*sin(14*y*pi)*sin(6*z*pi) - 32*cos(14*x*pi)*sin(6*y*pi)*sin(6*z*pi) - 32*cos(6*y*pi)*sin(6*x*pi)*sin(14*z*pi) - 32*cos(6*y*pi)*sin(14*x*pi)*sin(6*z*pi) - 32*cos(14*y*pi)*sin(6*x*pi)*sin(6*z*pi) - 32*cos(6*z*pi)*sin(6*x*pi)*sin(14*y*pi) - 32*cos(6*z*pi)*sin(14*x*pi)*sin(6*y*pi) - 32*cos(14*z*pi)*sin(6*x*pi)*sin(6*y*pi)
        FA += SF.ai[idx_a]*fA733*Multi[idx_a]
        hkl.append([7,3,3])
        idx_a += 1

    if 23 in usedBasis:
        fA644 = - 64*cos(12*x*pi)*sin(8*y*pi)*sin(8*z*pi) - 64*cos(12*y*pi)*sin(8*x*pi)*sin(8*z*pi) - 64*cos(12*z*pi)*sin(8*x*pi)*sin(8*y*pi)
        FA += SF.ai[idx_a]*fA644*Multi[idx_a]
        hkl.append([6,4,4])
        idx_a += 1

    if 24 in usedBasis:
        fA660 = - 64*sin(12*x*pi)*sin(12*y*pi) - 64*sin(12*x*pi)*sin(12*z*pi) - 64*sin(12*y*pi)*sin(12*z*pi)
        FA += SF.ai[idx_a]*fA660*Multi[idx_a]
        hkl.append([6,6,0])
        idx_a += 1

    if 25 in usedBasis:
        fA822 = - 64*cos(16*x*pi)*sin(4*y*pi)*sin(4*z*pi) - 64*cos(16*y*pi)*sin(4*x*pi)*sin(4*z*pi) - 64*cos(16*z*pi)*sin(4*x*pi)*sin(4*y*pi)
        FA += SF.ai[idx_a]*fA822*Multi[idx_a]
        hkl.append([8,2,2])
        idx_a += 1

    if 26 in usedBasis:
        fA555 = - 96*cos(10*x*pi)*cos(10*y*pi)*cos(10*z*pi) - 96*cos(10*x*pi)*sin(10*y*pi)*sin(10*z*pi) - 96*cos(10*y*pi)*sin(10*x*pi)*sin(10*z*pi) - 96*cos(10*z*pi)*sin(10*x*pi)*sin(10*y*pi)
        FA += SF.ai[idx_a]*fA555*Multi[idx_a]
        hkl.append([5,5,5])
        idx_a += 1

    if 27 in usedBasis:
        fA751 = 16*cos(2*x*pi)*cos(10*y*pi)*cos(14*z*pi) + 16*cos(2*x*pi)*cos(14*y*pi)*cos(10*z*pi) + 16*cos(10*x*pi)*cos(2*y*pi)*cos(14*z*pi) + 16*cos(10*x*pi)*cos(14*y*pi)*cos(2*z*pi) + 16*cos(14*x*pi)*cos(2*y*pi)*cos(10*z*pi) + 16*cos(14*x*pi)*cos(10*y*pi)*cos(2*z*pi) - 16*cos(2*x*pi)*sin(10*y*pi)*sin(14*z*pi) - 16*cos(2*x*pi)*sin(14*y*pi)*sin(10*z*pi) - 16*cos(10*x*pi)*sin(2*y*pi)*sin(14*z*pi) - 16*cos(10*x*pi)*sin(14*y*pi)*sin(2*z*pi) + 16*cos(14*x*pi)*sin(2*y*pi)*sin(10*z*pi) + 16*cos(14*x*pi)*sin(10*y*pi)*sin(2*z*pi) - 16*cos(2*y*pi)*sin(10*x*pi)*sin(14*z*pi) - 16*cos(2*y*pi)*sin(14*x*pi)*sin(10*z*pi) - 16*cos(10*y*pi)*sin(2*x*pi)*sin(14*z*pi) - 16*cos(10*y*pi)*sin(14*x*pi)*sin(2*z*pi) + 16*cos(14*y*pi)*sin(2*x*pi)*sin(10*z*pi) + 16*cos(14*y*pi)*sin(10*x*pi)*sin(2*z*pi) - 16*cos(2*z*pi)*sin(10*x*pi)*sin(14*y*pi) - 16*cos(2*z*pi)*sin(14*x*pi)*sin(10*y*pi) - 16*cos(10*z*pi)*sin(2*x*pi)*sin(14*y*pi) - 16*cos(10*z*pi)*sin(14*x*pi)*sin(2*y*pi) + 16*cos(14*z*pi)*sin(2*x*pi)*sin(10*y*pi) + 16*cos(14*z*pi)*sin(10*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA751*Multi[idx_a]
        hkl.append([7,5,1])
        idx_a += 1

    if 28 in usedBasis:
        fA662 = 64*cos(4*x*pi)*cos(12*y*pi)*cos(12*z*pi) + 64*cos(12*x*pi)*cos(4*y*pi)*cos(12*z*pi) + 64*cos(12*x*pi)*cos(12*y*pi)*cos(4*z*pi)
        FA += SF.ai[idx_a]*fA662*Multi[idx_a]
        hkl.append([6,6,2])
        idx_a += 1

    if 29 in usedBasis:
        fA840 = 32*cos(8*x*pi)*(2*cos(8*y*pi)**2 - 1) + 32*cos(8*y*pi)*(2*cos(8*x*pi)**2 - 1) + 32*cos(8*x*pi)*(2*cos(8*z*pi)**2 - 1) + 32*cos(8*z*pi)*(2*cos(8*x*pi)**2 - 1) + 32*cos(8*y*pi)*(2*cos(8*z*pi)**2 - 1) + 32*cos(8*z*pi)*(2*cos(8*y*pi)**2 - 1)
        FA += SF.ai[idx_a]*fA840*Multi[idx_a]
        hkl.append([8,4,0])
        idx_a += 1

    if 30 in usedBasis:
        fA753 = 16*cos(6*x*pi)*cos(10*y*pi)*cos(14*z*pi) + 16*cos(6*x*pi)*cos(14*y*pi)*cos(10*z*pi) + 16*cos(10*x*pi)*cos(6*y*pi)*cos(14*z*pi) + 16*cos(10*x*pi)*cos(14*y*pi)*cos(6*z*pi) + 16*cos(14*x*pi)*cos(6*y*pi)*cos(10*z*pi) + 16*cos(14*x*pi)*cos(10*y*pi)*cos(6*z*pi) - 16*cos(6*x*pi)*sin(10*y*pi)*sin(14*z*pi) - 16*cos(6*x*pi)*sin(14*y*pi)*sin(10*z*pi) + 16*cos(10*x*pi)*sin(6*y*pi)*sin(14*z*pi) + 16*cos(10*x*pi)*sin(14*y*pi)*sin(6*z*pi) - 16*cos(14*x*pi)*sin(6*y*pi)*sin(10*z*pi) - 16*cos(14*x*pi)*sin(10*y*pi)*sin(6*z*pi) - 16*cos(6*y*pi)*sin(10*x*pi)*sin(14*z*pi) - 16*cos(6*y*pi)*sin(14*x*pi)*sin(10*z*pi) + 16*cos(10*y*pi)*sin(6*x*pi)*sin(14*z*pi) + 16*cos(10*y*pi)*sin(14*x*pi)*sin(6*z*pi) - 16*cos(14*y*pi)*sin(6*x*pi)*sin(10*z*pi) - 16*cos(14*y*pi)*sin(10*x*pi)*sin(6*z*pi) - 16*cos(6*z*pi)*sin(10*x*pi)*sin(14*y*pi) - 16*cos(6*z*pi)*sin(14*x*pi)*sin(10*y*pi) + 16*cos(10*z*pi)*sin(6*x*pi)*sin(14*y*pi) + 16*cos(10*z*pi)*sin(14*x*pi)*sin(6*y*pi) - 16*cos(14*z*pi)*sin(6*x*pi)*sin(10*y*pi) - 16*cos(14*z*pi)*sin(10*x*pi)*sin(6*y*pi)
        FA += SF.ai[idx_a]*fA753*Multi[idx_a]
        hkl.append([7,5,3])
        idx_a += 1

    if 31 in usedBasis:
        fA911 = - 32*cos(2*x*pi)*cos(2*y*pi)*cos(18*z*pi) - 32*cos(2*x*pi)*cos(18*y*pi)*cos(2*z*pi) - 32*cos(18*x*pi)*cos(2*y*pi)*cos(2*z*pi) - 32*cos(2*x*pi)*sin(2*y*pi)*sin(18*z*pi) - 32*cos(2*x*pi)*sin(18*y*pi)*sin(2*z*pi) - 32*cos(18*x*pi)*sin(2*y*pi)*sin(2*z*pi) - 32*cos(2*y*pi)*sin(2*x*pi)*sin(18*z*pi) - 32*cos(2*y*pi)*sin(18*x*pi)*sin(2*z*pi) - 32*cos(18*y*pi)*sin(2*x*pi)*sin(2*z*pi) - 32*cos(2*z*pi)*sin(2*x*pi)*sin(18*y*pi) - 32*cos(2*z*pi)*sin(18*x*pi)*sin(2*y*pi) - 32*cos(18*z*pi)*sin(2*x*pi)*sin(2*y*pi)
        FA += SF.ai[idx_a]*fA911*Multi[idx_a]
        hkl.append([9,1,1])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    # 227: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return FA+FB, idx_theta, hkl
