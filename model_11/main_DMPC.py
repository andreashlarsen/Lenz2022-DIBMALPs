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
['154_J6_DMPC_R05',0.0],\
['154_J7_DMPC_R1',0.0],\
['154_J8_DMPC_R2',0.0],\
['196_J9_DMPC_10CHOL_R2',0.014],\
['196_J10_DMPC_20CHOL_R2',0.014],\
['196_J11_DMPC_30CHOL_R2',0.033]\
]

PLOT = 1

for d in data_elements:
#for d in [data_elements[0]]:
    data = d[0]
    chol_pr_lip = d[1]

    out('########### IMPORTING DATA ###############')

    ## import data
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
        func  = micelle_ellipsoid_DMPC_0CHOL_DIBMA
    elif chol_pr_lip == 0.014:
        func  = micelle_ellipsoid_DMPC_14CHOL_DIBMA
    elif chol_pr_lip == 0.033:
        func  = micelle_ellipsoid_DMPC_33CHOL_DIBMA
    else:
        print('ERROR - not valid option for chol_pr_lip')
        exit()
    pname = ['poly_pr_lip','scale_V_poly0','N_lip','eps','sigma_roughness','scale','background']
    p0    = [ 0.1,          0.7,            60,     1.5,  2.0,              I0_0,   B_0,       ]
    pmin  = [ 0.0,          0.5,            10,     1.0,  0.0,              0.01,   -0.1,      ]
    pmax  = [ 1.0,          2.0,            400,    5.0,  10.0,             1000,   0.1,       ]
    pfit  = [ 1,            1,              1,      1,    1,                1,      1,         ]

    # N_lip is number of DMPCs per micelle

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

    r,R,dp_t,dp_h = reparam('DM',*popt,chol_pr_lip)

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
