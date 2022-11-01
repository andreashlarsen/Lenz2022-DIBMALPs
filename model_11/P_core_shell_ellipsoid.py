import numpy as np
from psi_ellipsoid import *

def P_core_shell_ellipsoid(q,r,R,eps,dp_core,dp_shell):
    """
    form factor for core-shell ellipsoid
    """
    
    V_R = get_V_ellipsoid(R,R,R*eps)
    V_r = get_V_ellipsoid(r,r,r*eps)

    alpha = np.linspace(0,np.pi/2,30)
    P_sum = 0.0

    for a in alpha:
        A_core_shell_ellipsoid = V_R*dp_shell*psi_ellipsoid(q,R,eps,a) - V_r*dp_shell*psi_ellipsoid(q,r,eps,a) + V_r*dp_core*psi_ellipsoid(q,r,eps,a)
        psi_core_shell_ellipsoid = A_core_shell_ellipsoid/(V_R*dp_shell - V_r*dp_shell + V_r*dp_core)
        P_sum += psi_core_shell_ellipsoid**2 * np.sin(a)
    P_core_shell_ellipsoid = P_sum/P_sum[0]

    return P_core_shell_ellipsoid

def get_V_ellipsoid(a,b,c):
    """
    get volume of ellipsoid with radii a,b,c
    """
    V = 4/3*np.pi*a*b*c

    return V
