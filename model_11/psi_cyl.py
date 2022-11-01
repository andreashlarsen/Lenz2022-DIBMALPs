# form factor amplitude of a cylinder
# j1 is the Bessel functio of the first kind of order 1

import numpy as np
from scipy.special import j1

def psi_cyl(q,R,L,alpha):
    
    A = q*R*np.sin(alpha)
    B = q*L*np.cos(alpha)/2
    psi = 2*j1c(A) * sinc(B)
    
    return psi

def sinc(x):
    return np.sinc(x/np.pi)

def j1c(x):
    if x[0] == 0:
        return np.ones(len(x)) * 0.5 # limit for x->0
    else:
        return j1(x)/x
