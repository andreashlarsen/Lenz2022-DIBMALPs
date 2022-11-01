import numpy as np
from A_nd import A_nd

def disc(q,r,R,h,l,L,p_h,p_t,p_b,scale,background):
    
    ## integrate over alpha
    alpha_max = np.pi/2.0
    N_alpha = 50
    alpha = np.linspace(0,alpha_max,N_alpha)
    d_alpha = alpha_max/N_alpha
    
    sum_A2 = 0.0
    for a in alpha:
        A2 = A_nd(q,r,R,h,l,L,p_h,p_t,p_b,a)**2.0
        sum_A2 += A2*np.sin(a)

    ## calculate model intensity 
    Imod = sum_A2*d_alpha
    Imod /= Imod[0]

    return scale * Imod + background

