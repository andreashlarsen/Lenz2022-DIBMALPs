import numpy as np
from psi_sphere import *

def psi_ellipsoid(q,R,eps,alpha):

   R_eff = R*(np.sin(alpha)**2 + eps**2*np.cos(alpha)**2)**0.5
   psi_ellipsoid = psi_sphere(q,R_eff)
 
   return psi_ellipsoid
