import numpy as np
from P_core_shell_ellipsoid import *

def micelle_ellipsoid_DMPC_CHOL_DIBMA(q,chol_pr_lip,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background):
    I = micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,'DM',chol_pr_lip)
    return I
def micelle_ellipsoid_DMPC_0CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background):
    I = micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,'DM',0.00)
    return I
def micelle_ellipsoid_DMPC_14CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background):
    I = micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,'DM',0.014)
    return I
def micelle_ellipsoid_DMPC_33CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background):
    I = micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,'DM',0.033)
    return I   


def micelle_ellipsoid_POPC_CHOL_DIBMA(q,chol_pr_lip,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background):
    I = micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,'PO',chol_pr_lip)
    return I
def micelle_ellipsoid_POPC_0CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background):
    I = micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,'PO',0.0)
    return I
def micelle_ellipsoid_POPC_8CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background):
    I = micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,'PO',0.10)
    return I
def micelle_ellipsoid_POPC_15CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background):
    I = micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,'PO',0.15)
    return I
def micelle_ellipsoid_POPC_18CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background):
    I = micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,'PO',0.18)
    return I
def micelle_ellipsoid_XXPC_CHOL_DIBMA(q,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,lip_tail,chol_pr_lip):

    ## calculate intensity 
    r,R,dp_t,dp_h = reparam(lip_tail,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,chol_pr_lip)
    Imod = P_core_shell_ellipsoid(q,r,R,eps,dp_t,dp_h)

    if sigma_roughness > 1e-8:
        x = q*sigma_roughness
        Imod *= np.exp(-x**2/2)
        
    I = scale*Imod + background

    return I
    
def reparam(lip_tail,poly_pr_lip,scale_V_poly,N_lip,eps,sigma_roughness,scale,background,chol_pr_lip):

    ## partial specific molecular volumes
    V_H2O      = 30.0
    V_PC       = 319.0 # angstrom cubed, from WIF example file: NanodiscWithTags.dat
    if lip_tail == 'DM':
        V_XX       = 682.4+108.6 # angstrom cubed, from WIF example file: PeptideDiscs.dat (in that file, the tail is divided into CH2 and CH3)
    elif lip_tail == 'PO':
        V_XX       = 818.8+108.6 # angstrom cubed, from WIF example file: NanodiscWithTags.dat (in that file, the tail is divided into CH2 and CH3)
    else:
        print('ERROR in micelle_XXPC_CHOL_DIBMA(): lip_tail has to be \'DM\' or \'PC\'\n')
    V_chol     = 678.0 # angstrom cubed, from: https://pubs.acs.org/doi/full/10.1021/jp310345j (SI)
    V_poly0    = 688.0 # angstrom cubed, mail from Alessandra 
    V_tail0    = chol_pr_lip*V_chol+V_XX # mix of POPC and cholesterol

    V_poly = scale_V_poly * V_poly0
    V_tail = V_tail0 + poly_pr_lip*V_poly
    V_head = V_PC + poly_pr_lip*V_poly
    # use hydrated POPC??. https://www.sciencedirect.com/science/article/pii/S0006349507708998

    ## scattering lenghts
    b_H = 1
    b_C = 6 
    b_N = 7
    b_O = 8
    b_P = 15

    b_H2O  = 2*b_H+1*b_O
    b_PC   = 10*b_C + 8*b_O + 1*b_P + 1*b_N + 18*b_H # C8 O8 P N H18
    b_chol = 27*b_C + 1*b_O + 46*b_H # C27 O H46
    if lip_tail == 'DM':
        b_XX   = 26*b_C + 53*b_H # C26 H53 for each tail  
    elif lip_tail == 'PO':
        b_XX   = 32*b_C + 65*b_H # C32 H65 
    b_poly = 20*b_C + 8*b_O + 1*b_N + 36*b_H # C20 O8 N H36

    b_tail = poly_pr_lip*b_poly+chol_pr_lip*b_chol+b_XX
    b_head = poly_pr_lip*b_poly+b_PC

    ## scattering lenght densities
    p_H2O = b_H2O/V_H2O
    p_t   = b_tail/V_tail 
    p_h   = b_head/V_head 
   
    ## excess scattering length densities
    dp_t = p_t - p_H2O
    dp_h = p_h - p_H2O
    
    ## reparametrize geometric params

    V_core = N_lip*V_tail 
    V_shell = N_lip*V_head
    V_total = V_core+V_shell

    r = get_sphere_radius(V_core)
    R = get_sphere_radius(V_total)
        
    return r,R,dp_t,dp_h

def get_sphere_radius(V):
    R_cubed = 3*V/(4*np.pi)
    R = (R_cubed)**(1/3)

    return R

