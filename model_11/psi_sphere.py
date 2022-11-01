import numpy as np

def psi_sphere(q,R):

   x = q*R
   psi_sphere = 3*(np.sin(x)-x*np.cos(x))/x**3
 
   return psi_sphere
