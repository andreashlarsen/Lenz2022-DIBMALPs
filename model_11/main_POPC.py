import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from micelle_ellipsoid_XXPC_CHOL_DIBMA import *
from fit import *
from plot_results import *
from save_results import *
from store_files import *
from out import *
from clean_up import *

# data with DMPC and prc chol (fixed)
data_elements = [\
['154_J1_POPC_R2',0.0],\
['154_J2_POPC_R4',0.0],\
['154_J3_POPC_10CHOL_R4',0.08],\
['154_J4_POPC_20CHOL_R4',0.18],\
#['154_J5_POPC_20CHOL_R8',0.2],\
['196_J12_POPC_30CHOL_R4',0.15]\
]

PLOT = 1

for d in data_elements:
#for d in [data_elements[0]]:
    data = d[0]
    chol_pr_lip = d[1]

    out('########### IMPORTING DATA ###############')

    ## import data
    skip_first = 0
    out('Data: %s' % data)
    path = '../IFT/%s_RB/rescale.d' % data
    q,I,dI = np.genfromtxt(path,skip_header=3,usecols=[0,1,2],unpack=True)

    print('########### GENERAL FITTING SETTINGS  ###############')

    # scale and background initial guesses (average of, respectively, first and last data points)
    N_I0 = int(len(I)/100)
    I0_0 = np.mean(I[0:N_I0])
    B_0  = 0.0

    FIX = 0
    FIT_BACKGROUND_ONLY = 0

    out('########### MODEL PARAMETERS ###############')

    ## model parameters
    if chol_pr_lip == 0.0:
        func  = micelle_ellipsoid_POPC_0CHOL_DIBMA
    elif chol_pr_lip == 0.08:
        func  = micelle_ellipsoid_POPC_8CHOL_DIBMA
    elif chol_pr_lip == 0.18:
        func  = micelle_ellipsoid_POPC_18CHOL_DIBMA
    elif chol_pr_lip == 0.15:
        func  = micelle_ellipsoid_POPC_15CHOL_DIBMA
    else:
        print('ERROR - not valid option for chol_pr_lip')
        exit()
    pname = ['poly_pr_lip','scale_V_poly0','N_lip','eps','sigma_roughness','scale','background']
    p0    = [0.1,          0.7,            60,     1.5,  2.0,              I0_0,   B_0,       ]
    pmin  = [0.0,          0.5,            10,     1.2,  0.0,              0.01,   -0.1,      ]
    pmax  = [1.0,          2.0,            400,    5.0,  10.0,             1000,   0.1,       ]
    pfit  = [1,            1,              1,      1,    1,                1,      1,         ]

    # N_lip is number of POPCs per micelle

    if FIX:
        for i in range(len(pname)):
            pfit[i] = 0
    elif FIT_BACKGROUND_ONLY:
        for i in range(len(pname)-1):
            pfit[i] = 0
        
    # fit or fix parameters
    eps = 1e-10
    for i in range(len(pname)):
        if pfit[i] == 0:
            pmin[i] = p0[i]-eps
            pmax[i] = p0[i]+eps

    print('########### CALCULATING AND FITTING MODEL ###############')

    tol = 1e-4 # ftol and xtol (precision before convergence, default is 1e-8)
    chi2r,*popt = fit(q,I,dI,func,pname,p0,pmin,pmax,pfit,tol)

    out('########### DERIVED PARAMETERS ###############')

    r,R,dp_t,dp_h = reparam('PO',*popt,chol_pr_lip)

    out('r = %-12.5f' % r)
    out('R = %-12.5f' % R)
    out('dp_t = %-12.5f' % dp_t)
    out('dp_h = %-12.5f' % dp_h)

    print('########### PLOTTING DATA AND FIT ###############')

    if PLOT:
        plot_results(q,I,dI,func,pfit,*popt)

    print('########### SAVE FIT TO FILE  ###############')

    save_results(q,I,dI,func,pfit,*popt)

    print('########### STORE FILES  ###############')

    store_files(data)

clean_up()