import numpy as np
import matplotlib.pyplot as plt
import os

from rebin import *
from out import *

data_elements = [\
['154_J1_POPC_R2',0.0,32],\
['154_J2_POPC_R4',0.0,30],\
['154_J3_POPC_10CHOL_R4',0.1,32],\
['154_J4_POPC_20CHOL_R4',0.2,32],\
['154_J5_POPC_20CHOL_R8',0.2,30],\
['196_J12_POPC_30CHOL_R4',0.3,30],\
['154_J6_DMPC_R05',0.0,45],\
['154_J7_DMPC_R1',0.0,45],\
['154_J8_DMPC_R2',0.0,40],\
['196_J9_DMPC_10CHOL_R2',0.01,30],\
['196_J10_DMPC_20CHOL_R2',0.02,30],\
['196_J11_DMPC_30CHOL_R2',0.05,30]\
]

PLOT = 1

#for d in data_elements:
for d in [data_elements[8]]:
    data = d[0]
    chol_pr_lip = d[1]
    skip_first = d[2]

    out('########### IMPORTING DATA ###############')

    ## import data
    out('Data: %s' % data)
    path = 'sub_data/%s.dat' % data
    q,I,dI = np.genfromtxt(path,skip_header=3+skip_first,usecols=[0,1,2],unpack=True)
    
    out('########### REBIN AND SAVE DATA ###############')
    
    q_RB,I_RB,dI_RB = rebinSAS(q,I,dI,'log',1.02)
    folder = 'Data_rebin'
    os.system('mkdir -p %s' % folder)
    with open('%s/%s_RB.dat' % (folder,data),'w') as f:
        f.write('# rebinned data\n')
        f.write('# %-12s %-12s %-12s\n' % ('q','I','dI'))
        for (q_i,I_i,dI_i) in zip(q_RB,I_RB,dI_RB):
            f.write('  %-12.5e %-12.5e %-12.5e\n' % (q_i,I_i,dI_i))

    print('########### PLOTTING DATA AND REBINNED DATA ###############')
    
    if PLOT:
        scale = 1
        plt.errorbar(q,I,yerr=dI,linestyle='none',marker='.',label='not rebinned',zorder=0)
        plt.errorbar(q_RB,I_RB*scale,yerr=dI_RB*scale,linestyle='none',marker='.',label='rebinned',zorder=1)
        
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('q')
        plt.ylabel('I(q)')
        plt.title('%s' % data)
        plt.legend(frameon=False)
        if PLOT:
            plt.show()
