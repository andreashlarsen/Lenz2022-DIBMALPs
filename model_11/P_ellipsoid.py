import numpy as np
from psi_ellipsoid import *

def P_ellipsoid(q,R,eps):
   
   alpha = np.linspace(0,np.pi/2,30)
   P_sum = 0.0

   for a in alpha:
       P_sum += psi_ellipsoid(q,R,eps,a)**2 * np.sin(a)
   P_ellipsoid = P_sum/P_sum[0]
 
   return P_ellipsoid
