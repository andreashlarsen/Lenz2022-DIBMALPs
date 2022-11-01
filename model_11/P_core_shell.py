import numpy as np
from psi_sphere import *

def P_core_shell(q,r,R,dp_core,dp_shell):
    """
    form factor for core-shell
    """

    V_R = get_V_sphere(R)
    V_r = get_V_sphere(r)

    A_core_shell = V_R*dp_shell*psi_sphere(q,R) - V_r*dp_shell*psi_sphere(q,r) + V_r*dp_core*psi_sphere(q,r)
    psi_core_shell = A_core_shell/(V_R*dp_shell - V_r*dp_shell + V_r*dp_core)
    P_core_shell = psi_core_shell**2

    return P_core_shell

def get_V_sphere(R):
    """
    get volume of sphere with radius R
    """
    V = 4/3*np.pi*R**3

    return V

