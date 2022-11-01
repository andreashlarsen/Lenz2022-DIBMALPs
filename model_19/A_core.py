from psi_cyl import psi_cyl
from V_cyl import V_cyl

def A_core(q,r,l,L,p_h,p_t,alpha):
   
   A_core = p_h*F(q,r,L,alpha)-p_h*F(q,r,l,alpha)+p_t*F(q,r,l,alpha)
 
   return A_core

def F(q,R,L,alpha):
    return V_cyl(R,L)*psi_cyl(q,R,L,alpha)
