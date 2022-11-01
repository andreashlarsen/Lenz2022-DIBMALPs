import numpy as np
import matplotlib.pyplot as plt
from rebin import *

REBIN = True

data = [\
[1, '154_J1_POPC_R2',        'POPC', '2',   0, 0, 0, 1e1],\
[2, '154_J2_POPC_R4',        'POPC', '4',   0, 0, 0, 1e0],\
[3, '154_J3_POPC_10CHOL_R4', 'POPC', '4',  10, 0, 1, 1e3],\
[4, '154_J4_POPC_20CHOL_R4', 'POPC', '4',  20, 0, 1, 1e2],\
[5, '154_J5_POPC_20CHOL_R8', 'POPC', '8',  20, 0, 1, 1e1],\
[6, '154_J6_DMPC_R05',       'DMPC', '0.5', 0, 1, 0, 1e2],\
[7, '154_J7_DMPC_R1',        'DMPC', '1',   0, 1, 0, 1e1],\
[8, '154_J8_DMPC_R2',        'DMPC', '2',   0, 1, 0, 1e0],\
[9, '196_J9_DMPC_10CHOL_R2', 'DMPC', '2',  10, 1, 1, 1e2],\
[10,'196_J10_DMPC_20CHOL_R2','DMPC', '2',  20, 1, 1, 1e1],\
[11,'196_J11_DMPC_30CHOL_R2','DMPC', '2',  30, 1, 1, 1e0],\
[12,'196_J12_POPC_30CHOL_R4','POPC', '4',  30, 0, 1, 1e0]\
]

fig,ax = plt.subplots(2,2,figsize=(9,9))

for d in data: 
    number = d[0]
    folder = d[1]
    lipid = d[2]
    ratio = d[3]
    chol = d[4]
    row = d[5]
    col = d[6]
    scale = d[7]

    ## import data and fit
    data = '%s/Idat.dat' % folder
    fit = '%s/Ifit.dat' % folder
    q,I,dI = np.genfromtxt(data,skip_header=1,usecols=[0,1,2],unpack=True)
    qfit,Ifit = np.genfromtxt(fit,skip_header=2,usecols=[0,1],unpack=True)

    ## get reduced chi-square
    f = open(fit)
    line = f.readline()
    CONTINUE = 1
    while CONTINUE == 1:
        if 'reduced chi-square' in line:
            chi2r = float(line.split('=')[1])
            CONTINUE = 0
        line = f.readline()
    f.close()

    ## rebin
    if REBIN:
       q,I,dI = rebin3(q,I,dI,'log',1.08) 
       #q,I,dI = rebinSAS(q,I,dI,'lin',50) 
    
    ## plot
    label = r'J%d, %s, %d%s chol, R %s, $\chi^2_r$ %1.1f' % (number,lipid,chol,'%',ratio,chi2r)
    ax[row,col].errorbar(q,I*scale,dI*scale,linestyle='none',marker='.',label = label,zorder=0)
    ax[row,col].plot(qfit,Ifit*scale,color='black',zorder=1)

    ax[row,col].legend(frameon=False,fontsize=8)

for i in range(2):
    for j in range(2):
        ax[i,j].set_xscale('log')
        ax[i,j].set_yscale('log')
        ax[i,j].set_xlabel(r'$q$ [$\mathrm{\AA}^{-1}$]')
        ax[i,j].set_ylabel('Intensity [a.u.]')

plt.tight_layout()
plt.savefig('all_fits')
plt.show()


