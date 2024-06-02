# Generated at 2024-03-12 13:53:05
# Qingshu Dong

import numpy as np

def  calF_154_0d5(SF,startBasis=0):
    [x,y,z] = np.meshgrid(np.linspace(0,1-1.0/SF.Nx,SF.Nx),np.linspace(0,1-1.0/SF.Ny,SF.Ny),np.linspace(0,1-1.0/SF.Nz,SF.Nz),indexing='ij')
    pi = np.pi
    cos = np.cos
    sin = np.sin

    all_Multi = np.array([6, 6, 6, 12, 12, 12, 12, 6, 24, 6, 12, 12, 12, 12, 12, 6, 24, 12, 12, 12, 24, 12, 12, 24, 24, 12, 6, 24, 6, 2, 12, 12])
    Multi = all_Multi[startBasis:startBasis+SF.basisNumber]
    hkl = []

    usedBasis = startBasis + np.arange(SF.basisNumber)
    if usedBasis[-1] > 32:
        raise ValueError('Max basis number > 32, not supported for spaceGroupNo 154.0')

    FA = 0
    FB = 0
    idx_theta = 0
    idx_a = 0

    if 0 in usedBasis:
        fA100 = 2*cos(2*x*pi) + 2*cos(2*y*pi) + 2*cos(2*pi*(x - y))
        FA += SF.ai[idx_a]*fA100*Multi[idx_a]
        hkl.append([1,0,0])
        idx_a += 1

    if 1 in usedBasis:
        fA110 = 2*cos(2*pi*(2*x - y)) + 2*cos(2*pi*(x + y)) + 2*cos(2*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA110*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB110 = 2*sin(2*pi*(x + y)) - 2*sin(2*pi*(2*x - y)) + 2*sin(2*pi*(x - 2*y))
        FB += SF.ai[idx_a]*fB110*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,0])
        idx_a += 1

    if 2 in usedBasis:
        fA200 = 2*cos(4*x*pi) + 2*cos(4*y*pi) + 2*cos(4*pi*(x - y))
        FA += SF.ai[idx_a]*fA200*Multi[idx_a]
        hkl.append([2,0,0])
        idx_a += 1

    if 3 in usedBasis:
        fA101 = cos((pi*(6*x + 6*z + 1))/3) + cos((pi*(6*y - 6*z + 1))/3) - cos(2*pi*(y - x + z))
        FA += SF.ai[idx_a]*fA101*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB101 = -3**(1/2)*(cos((pi*(6*x + 6*z + 1))/3) + cos((pi*(6*y - 6*z + 1))/3) - cos(2*pi*(y - x + z)))
        FB += SF.ai[idx_a]*fB101*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,1])
        idx_a += 1

    if 4 in usedBasis:
        fA111 = cos(2*pi*(x + y - z)) + cos(2*pi*(x + y + z)) + cos((2*pi*(3*x - 6*y - 3*z + 1))/3) + cos((2*pi*(3*y - 6*x + 3*z + 1))/3) + cos((2*pi*(3*x - 6*y + 3*z + 2))/3) + cos((2*pi*(6*x - 3*y + 3*z - 2))/3)
        FA += SF.ai[idx_a]*fA111*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB111 = sin((2*pi*(3*x - 6*y + 3*z + 2))/3) + sin((pi*(12*x - 6*y + 6*z - 1))/3) + sin(2*pi*(x + y - z)) + sin(2*pi*(x + y + z)) + cos((pi*(12*x - 24*y - 12*z + 1))/6) + cos((pi*(12*y - 24*x + 12*z + 1))/6)
        FB += SF.ai[idx_a]*fB111*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,1])
        idx_a += 1

    if 5 in usedBasis:
        fA210 = cos(2*pi*(3*x - y)) + cos(2*pi*(2*x - 3*y)) + cos(2*pi*(3*x - 2*y)) + cos(2*pi*(x + 2*y)) + cos(2*pi*(2*x + y)) + cos(2*pi*(x - 3*y))
        FA += SF.ai[idx_a]*fA210*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB210 = sin(2*pi*(2*x - 3*y)) - sin(2*pi*(3*x - y)) - sin(2*pi*(3*x - 2*y)) + sin(2*pi*(x + 2*y)) + sin(2*pi*(2*x + y)) + sin(2*pi*(x - 3*y))
        FB += SF.ai[idx_a]*fB210*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,0])
        idx_a += 1

    if 6 in usedBasis:
        fA201 = cos((pi*(12*x + 6*z + 1))/3) + cos((pi*(12*y - 6*z + 1))/3) - cos(2*pi*(2*y - 2*x + z))
        FA += SF.ai[idx_a]*fA201*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB201 = -3**(1/2)*(cos((pi*(12*x + 6*z + 1))/3) + cos((pi*(12*y - 6*z + 1))/3) - cos(2*pi*(2*y - 2*x + z)))
        FB += SF.ai[idx_a]*fB201*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,1])
        idx_a += 1

    if 7 in usedBasis:
        fA300 = 2*cos(6*x*pi) + 2*cos(6*y*pi) + 2*cos(6*pi*(x - y))
        FA += SF.ai[idx_a]*fA300*Multi[idx_a]
        hkl.append([3,0,0])
        idx_a += 1

    if 8 in usedBasis:
        fA211 = cos(2*pi*(2*x + y + z)) + cos(2*pi*(x + 2*y - z)) + cos((2*pi*(3*x - 9*y + 3*z + 2))/3) + cos((2*pi*(9*x - 3*y + 3*z - 2))/3) + cos((2*pi*(6*x - 9*y - 3*z + 1))/3) + cos((2*pi*(6*y - 9*x + 3*z + 1))/3)
        FA += SF.ai[idx_a]*fA211*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB211 = sin((2*pi*(3*x - 9*y + 3*z + 2))/3) + sin((pi*(18*x - 6*y + 6*z - 1))/3) + sin(2*pi*(2*x + y + z)) + sin(2*pi*(x + 2*y - z)) + cos((pi*(24*x - 36*y - 12*z + 1))/6) + cos((pi*(24*y - 36*x + 12*z + 1))/6)
        FB += SF.ai[idx_a]*fB211*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,1])
        idx_a += 1

    if 9 in usedBasis:
        fA220 = 2*cos(4*pi*(2*x - y)) + 2*cos(4*pi*(x + y)) + 2*cos(4*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA220*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB220 = 2*sin(4*pi*(x + y)) - 2*sin(4*pi*(2*x - y)) + 2*sin(4*pi*(x - 2*y))
        FB += SF.ai[idx_a]*fB220*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,0])
        idx_a += 1

    if 10 in usedBasis:
        fA301 = cos((pi*(18*x + 6*z + 1))/3) + cos((pi*(18*y - 6*z + 1))/3) - cos(2*pi*(3*y - 3*x + z))
        FA += SF.ai[idx_a]*fA301*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB301 = -3**(1/2)*(cos((pi*(18*x + 6*z + 1))/3) + cos((pi*(18*y - 6*z + 1))/3) - cos(2*pi*(3*y - 3*x + z)))
        FB += SF.ai[idx_a]*fB301*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,1])
        idx_a += 1

    if 11 in usedBasis:
        fA310 = cos(2*pi*(4*x - y)) + cos(2*pi*(3*x - 4*y)) + cos(2*pi*(4*x - 3*y)) + cos(2*pi*(x + 3*y)) + cos(2*pi*(3*x + y)) + cos(2*pi*(x - 4*y))
        FA += SF.ai[idx_a]*fA310*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB310 = sin(2*pi*(3*x - 4*y)) - sin(2*pi*(4*x - y)) - sin(2*pi*(4*x - 3*y)) + sin(2*pi*(x + 3*y)) + sin(2*pi*(3*x + y)) + sin(2*pi*(x - 4*y))
        FB += SF.ai[idx_a]*fB310*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,0])
        idx_a += 1

    if 12 in usedBasis:
        fA102 = cos((pi*(12*z - 6*y + 1))/3) + sin((pi*(12*x + 24*z + 1))/6) - cos(2*pi*(y - x + 2*z))
        FA += SF.ai[idx_a]*fA102*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB102 = 3**(1/2)*(cos((pi*(12*z - 6*y + 1))/3) + sin((pi*(12*x + 24*z + 1))/6) - cos(2*pi*(y - x + 2*z)))
        FB += SF.ai[idx_a]*fB102*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,0,2])
        idx_a += 1

    if 13 in usedBasis:
        fA221 = cos(2*pi*(2*x + 2*y + z)) + cos(2*pi*(2*x + 2*y - z)) + cos((2*pi*(6*x - 12*y - 3*z + 1))/3) + cos((2*pi*(6*y - 12*x + 3*z + 1))/3) + cos((2*pi*(6*x - 12*y + 3*z + 2))/3) + cos((2*pi*(12*x - 6*y + 3*z - 2))/3)
        FA += SF.ai[idx_a]*fA221*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB221 = sin(2*pi*(2*x + 2*y - z)) + sin((2*pi*(6*x - 12*y + 3*z + 2))/3) + sin((pi*(24*x - 12*y + 6*z - 1))/3) + sin(2*pi*(2*x + 2*y + z)) + cos((pi*(24*x - 48*y - 12*z + 1))/6) + cos((pi*(24*y - 48*x + 12*z + 1))/6)
        FB += SF.ai[idx_a]*fB221*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,1])
        idx_a += 1

    if 14 in usedBasis:
        fA112 = cos(2*pi*(x + y - 2*z)) + cos(2*pi*(x + y + 2*z)) + cos((2*pi*(3*x - 6*y - 6*z + 2))/3) + cos((2*pi*(3*y - 6*x + 6*z + 2))/3) + cos((2*pi*(3*x - 6*y + 6*z + 4))/3) + cos((2*pi*(6*x - 3*y + 6*z - 4))/3)
        FA += SF.ai[idx_a]*fA112*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB112 = sin((2*pi*(3*x - 6*y + 6*z + 4))/3) - sin((pi*(6*x - 12*y - 12*z + 1))/3) - sin((pi*(6*y - 12*x + 12*z + 1))/3) + sin((pi*(12*x - 6*y + 12*z + 1))/3) + sin(2*pi*(x + y - 2*z)) + sin(2*pi*(x + y + 2*z))
        FB += SF.ai[idx_a]*fB112*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([1,1,2])
        idx_a += 1

    if 15 in usedBasis:
        fA400 = 2*cos(8*x*pi) + 2*cos(8*y*pi) + 2*cos(8*pi*(x - y))
        FA += SF.ai[idx_a]*fA400*Multi[idx_a]
        hkl.append([4,0,0])
        idx_a += 1

    if 16 in usedBasis:
        fA311 = cos(2*pi*(3*x + y + z)) + cos(2*pi*(x + 3*y - z)) + cos((2*pi*(3*x - 12*y + 3*z + 2))/3) + cos((2*pi*(12*x - 3*y + 3*z - 2))/3) + cos((2*pi*(9*x - 12*y - 3*z + 1))/3) + cos((2*pi*(9*y - 12*x + 3*z + 1))/3)
        FA += SF.ai[idx_a]*fA311*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB311 = sin((2*pi*(3*x - 12*y + 3*z + 2))/3) + sin((pi*(24*x - 6*y + 6*z - 1))/3) + sin(2*pi*(3*x + y + z)) + sin(2*pi*(x + 3*y - z)) + cos((pi*(36*x - 48*y - 12*z + 1))/6) + cos((pi*(36*y - 48*x + 12*z + 1))/6)
        FB += SF.ai[idx_a]*fB311*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,1])
        idx_a += 1

    if 17 in usedBasis:
        fA202 = cos((pi*(12*z - 12*y + 1))/3) + sin((pi*(24*x + 24*z + 1))/6) - cos(4*pi*(y - x + z))
        FA += SF.ai[idx_a]*fA202*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB202 = 3**(1/2)*(cos((pi*(12*z - 12*y + 1))/3) + sin((pi*(24*x + 24*z + 1))/6) - cos(4*pi*(y - x + z)))
        FB += SF.ai[idx_a]*fB202*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,0,2])
        idx_a += 1

    if 18 in usedBasis:
        fA320 = cos(2*pi*(2*x + 3*y)) + cos(2*pi*(3*x + 2*y)) + cos(2*pi*(2*x - 5*y)) + cos(2*pi*(5*x - 2*y)) + cos(2*pi*(3*x - 5*y)) + cos(2*pi*(5*x - 3*y))
        FA += SF.ai[idx_a]*fA320*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB320 = sin(2*pi*(2*x + 3*y)) + sin(2*pi*(3*x + 2*y)) + sin(2*pi*(2*x - 5*y)) - sin(2*pi*(5*x - 2*y)) + sin(2*pi*(3*x - 5*y)) - sin(2*pi*(5*x - 3*y))
        FB += SF.ai[idx_a]*fB320*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,0])
        idx_a += 1

    if 19 in usedBasis:
        fA401 = cos((pi*(24*x + 6*z + 1))/3) + cos((pi*(24*y - 6*z + 1))/3) - cos(2*pi*(4*y - 4*x + z))
        FA += SF.ai[idx_a]*fA401*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB401 = -3**(1/2)*(cos((pi*(24*x + 6*z + 1))/3) + cos((pi*(24*y - 6*z + 1))/3) - cos(2*pi*(4*y - 4*x + z)))
        FB += SF.ai[idx_a]*fB401*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,0,1])
        idx_a += 1

    if 20 in usedBasis:
        fA212 = cos(2*pi*(x + 2*y - 2*z)) + cos(2*pi*(2*x + y + 2*z)) + cos((2*pi*(3*x - 9*y + 6*z + 4))/3) + cos((2*pi*(9*x - 3*y + 6*z - 4))/3) + cos((2*pi*(6*x - 9*y - 6*z + 2))/3) + cos((2*pi*(6*y - 9*x + 6*z + 2))/3)
        FA += SF.ai[idx_a]*fA212*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB212 = sin((2*pi*(3*x - 9*y + 6*z + 4))/3) + sin((pi*(18*x - 6*y + 12*z + 1))/3) - sin((pi*(12*x - 18*y - 12*z + 1))/3) - sin((pi*(12*y - 18*x + 12*z + 1))/3) + sin(2*pi*(x + 2*y - 2*z)) + sin(2*pi*(2*x + y + 2*z))
        FB += SF.ai[idx_a]*fB212*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,1,2])
        idx_a += 1

    if 21 in usedBasis:
        fA410 = cos(2*pi*(5*x - y)) + cos(2*pi*(4*x - 5*y)) + cos(2*pi*(5*x - 4*y)) + cos(2*pi*(x + 4*y)) + cos(2*pi*(4*x + y)) + cos(2*pi*(x - 5*y))
        FA += SF.ai[idx_a]*fA410*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB410 = sin(2*pi*(4*x - 5*y)) - sin(2*pi*(5*x - y)) - sin(2*pi*(5*x - 4*y)) + sin(2*pi*(x + 4*y)) + sin(2*pi*(4*x + y)) + sin(2*pi*(x - 5*y))
        FB += SF.ai[idx_a]*fB410*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,1,0])
        idx_a += 1

    if 22 in usedBasis:
        fA302 = cos((pi*(12*z - 18*y + 1))/3) + sin((pi*(36*x + 24*z + 1))/6) - cos(2*pi*(3*y - 3*x + 2*z))
        FA += SF.ai[idx_a]*fA302*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB302 = 3**(1/2)*(cos((pi*(12*z - 18*y + 1))/3) + sin((pi*(36*x + 24*z + 1))/6) - cos(2*pi*(3*y - 3*x + 2*z)))
        FB += SF.ai[idx_a]*fB302*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,0,2])
        idx_a += 1

    if 23 in usedBasis:
        fA321 = cos(2*pi*(3*x + 2*y + z)) + cos(2*pi*(2*x + 3*y - z)) + cos((2*pi*(6*x - 15*y + 3*z + 2))/3) + cos((2*pi*(15*x - 6*y + 3*z - 2))/3) + cos((2*pi*(9*x - 15*y - 3*z + 1))/3) + cos((2*pi*(9*y - 15*x + 3*z + 1))/3)
        FA += SF.ai[idx_a]*fA321*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB321 = sin(2*pi*(2*x + 3*y - z)) + sin((2*pi*(6*x - 15*y + 3*z + 2))/3) + sin((pi*(30*x - 12*y + 6*z - 1))/3) + sin(2*pi*(3*x + 2*y + z)) + cos((pi*(36*x - 60*y - 12*z + 1))/6) + cos((pi*(36*y - 60*x + 12*z + 1))/6)
        FB += SF.ai[idx_a]*fB321*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,2,1])
        idx_a += 1

    if 24 in usedBasis:
        fA411 = cos(2*pi*(4*x + y + z)) + cos(2*pi*(x + 4*y - z)) + cos((2*pi*(3*x - 15*y + 3*z + 2))/3) + cos((2*pi*(15*x - 3*y + 3*z - 2))/3) + cos((2*pi*(12*x - 15*y - 3*z + 1))/3) + cos((2*pi*(12*y - 15*x + 3*z + 1))/3)
        FA += SF.ai[idx_a]*fA411*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB411 = sin((2*pi*(3*x - 15*y + 3*z + 2))/3) + sin((pi*(30*x - 6*y + 6*z - 1))/3) + sin(2*pi*(4*x + y + z)) + sin(2*pi*(x + 4*y - z)) + cos((pi*(48*x - 60*y - 12*z + 1))/6) + cos((pi*(48*y - 60*x + 12*z + 1))/6)
        FB += SF.ai[idx_a]*fB411*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,1,1])
        idx_a += 1

    if 25 in usedBasis:
        fA222 = cos(4*pi*(x + y - z)) + cos(4*pi*(x + y + z)) + cos((4*pi*(3*x - 6*y - 3*z + 1))/3) + cos((4*pi*(3*y - 6*x + 3*z + 1))/3) + cos((4*pi*(3*x - 6*y + 3*z + 2))/3) + cos((4*pi*(6*x - 3*y + 3*z - 2))/3)
        FA += SF.ai[idx_a]*fA222*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB222 = sin((4*pi*(3*x - 6*y + 3*z + 2))/3) - sin((pi*(12*x - 24*y - 12*z + 1))/3) - sin((pi*(12*y - 24*x + 12*z + 1))/3) + sin((pi*(24*x - 12*y + 12*z + 1))/3) + sin(4*pi*(x + y - z)) + sin(4*pi*(x + y + z))
        FB += SF.ai[idx_a]*fB222*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([2,2,2])
        idx_a += 1

    if 26 in usedBasis:
        fA500 = 2*cos(10*x*pi) + 2*cos(10*y*pi) + 2*cos(10*pi*(x - y))
        FA += SF.ai[idx_a]*fA500*Multi[idx_a]
        hkl.append([5,0,0])
        idx_a += 1

    if 27 in usedBasis:
        fA312 = cos(2*pi*(x + 3*y - 2*z)) + cos(2*pi*(3*x + y + 2*z)) + cos((2*pi*(3*x - 12*y + 6*z + 4))/3) + cos((2*pi*(12*x - 3*y + 6*z - 4))/3) + cos((2*pi*(9*x - 12*y - 6*z + 2))/3) + cos((2*pi*(9*y - 12*x + 6*z + 2))/3)
        FA += SF.ai[idx_a]*fA312*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB312 = sin((2*pi*(3*x - 12*y + 6*z + 4))/3) + sin((pi*(24*x - 6*y + 12*z + 1))/3) - sin((pi*(18*x - 24*y - 12*z + 1))/3) - sin((pi*(18*y - 24*x + 12*z + 1))/3) + sin(2*pi*(x + 3*y - 2*z)) + sin(2*pi*(3*x + y + 2*z))
        FB += SF.ai[idx_a]*fB312*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,1,2])
        idx_a += 1

    if 28 in usedBasis:
        fA330 = 2*cos(6*pi*(2*x - y)) + 2*cos(6*pi*(x + y)) + 2*cos(6*pi*(x - 2*y))
        FA += SF.ai[idx_a]*fA330*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB330 = 2*sin(6*pi*(x + y)) - 2*sin(6*pi*(2*x - y)) + 2*sin(6*pi*(x - 2*y))
        FB += SF.ai[idx_a]*fB330*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([3,3,0])
        idx_a += 1

    if 29 in usedBasis:
        fA003 = 6*cos(6*z*pi)
        FA += SF.ai[idx_a]*fA003*Multi[idx_a]
        hkl.append([0,0,3])
        idx_a += 1

    if 30 in usedBasis:
        fA420 = cos(4*pi*(3*x - y)) + cos(4*pi*(2*x - 3*y)) + cos(4*pi*(3*x - 2*y)) + cos(4*pi*(x + 2*y)) + cos(4*pi*(2*x + y)) + cos(4*pi*(x - 3*y))
        FA += SF.ai[idx_a]*fA420*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB420 = sin(4*pi*(2*x - 3*y)) - sin(4*pi*(3*x - y)) - sin(4*pi*(3*x - 2*y)) + sin(4*pi*(x + 2*y)) + sin(4*pi*(2*x + y)) + sin(4*pi*(x - 3*y))
        FB += SF.ai[idx_a]*fB420*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([4,2,0])
        idx_a += 1

    if 31 in usedBasis:
        fA501 = cos((pi*(30*x + 6*z + 1))/3) + cos((pi*(30*y - 6*z + 1))/3) - cos(2*pi*(5*y - 5*x + z))
        FA += SF.ai[idx_a]*fA501*cos(SF.theta[idx_theta])*Multi[idx_a]
        fB501 = -3**(1/2)*(cos((pi*(30*x + 6*z + 1))/3) + cos((pi*(30*y - 6*z + 1))/3) - cos(2*pi*(5*y - 5*x + z)))
        FB += SF.ai[idx_a]*fB501*sin(SF.theta[idx_theta])*Multi[idx_a]
        idx_theta += 1
        hkl.append([5,0,1])
        idx_a += 1

    # empty F record
    # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
    # 0 1 0 1 1 1 1 0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0 1 1 0 1 1 
    # 154_0d5: [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1]
    return FA+FB, idx_theta, hkl
