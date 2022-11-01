from psi_cyl import psi_cyl
from V_cyl import V_cyl

def A_nd(q,r,R,h,l,L,p_h,p_t,p_b,alpha):
   
   A_core = p_h*F(q,r,L,alpha)-p_h*F(q,r,l,alpha)+p_t*F(q,r,l,alpha)
 
   A_belt = p_b*F(q,R,h,alpha)-p_b*F(q,r,h,alpha)

   A = A_core + A_belt

   return A


def F(q,R,L,alpha):
    return V_cyl(R,L)*psi_cyl(q,R,L,alpha)
