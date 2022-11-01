import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from rebin import *
import os

def interp(x_in,y_in,x_out):
    f = interpolate.interp1d(x_in,y_in)
    y_out = f(x_out)

    return y_out

REBIN = 1 
SHOW_PLOT = 1

colors = ['dodgerblue','turquoise','mediumseagreen','y','orange','red']
#colors = ['blue','turquoise','green','y','orange','red']
dataset = [\
[1, '154_J1_POPC_R2',        'POPC', '2',   0, 0, 0, 1e1,colors[0]],\
[2, '154_J2_POPC_R4',        'POPC', '4',   0, 0, 0, 1e0,colors[2]],\
[3, '154_J3_POPC_10CHOL_R4', 'POPC', '4',  10, 0, 1, 1e2,colors[0]],\
[4, '154_J4_POPC_20CHOL_R4', 'POPC', '4',  20, 0, 1, 1e1,colors[1]],\
#[5, '154_J5_POPC_20CHOL_R8', 'POPC', '8',  20, 0, 1, 1e1,'black'],\
[6, '154_J6_DMPC_R05',       'DMPC', '0.5', 0, 1, 0, 1e2,colors[3]],\
[7, '154_J7_DMPC_R1',        'DMPC', '1',   0, 1, 0, 1e1,colors[4]],\
[8, '154_J8_DMPC_R2',        'DMPC', '2',   0, 1, 0, 1e0,colors[5]],\
[9, '196_J9_DMPC_10CHOL_R2', 'DMPC', '2',  10, 1, 1, 1e2,colors[3]],\
[10,'196_J10_DMPC_20CHOL_R2','DMPC', '2',  20, 1, 1, 1e1,colors[4]],\
[11,'196_J11_DMPC_30CHOL_R2','DMPC', '2',  30, 1, 1, 1e0,colors[5]],\
[12,'196_J12_POPC_30CHOL_R4','POPC', '4',  30, 0, 1, 1e0,colors[2]]\
]

model_folder = 'IFT'

fig,ax = plt.subplots(2,2,figsize=(9,9))

for d in dataset: 
    number = d[0]
    folder = d[1]
    lipid = d[2]
    ratio = d[3]
    chol = d[4]
    row = d[5]
    col = d[6]
    scale = d[7]
    color = d[8]

    ## import data and fit
    file = 'IFT/%s_RB/pr.d' % folder
    r,pr = np.genfromtxt(file,usecols=[0,1],unpack=True)

    ## normalize with max of pr
    pr = pr/np.amax(pr)

    ## plot
    linewidth=2
    label = r'%s, %d%s chol, $R$ %s' % (lipid,chol,'%',ratio)
    ax[row,col].plot(r,pr,linewidth=linewidth,color=color,label = label,zorder=1)
    ax[row,col].legend(frameon=False,fontsize=9)

xlim = [0,210]
for i in range(2):
    for j in range(2):
        ax[i,j].plot(xlim,[0,0],linestyle='--',linewidth=linewidth,color='lightgrey',zorder=0)
        ax[i,j].set_xlim(xlim)
        ax[i,j].set_xlabel(r'$r$ [$\mathrm{\AA}$]')
        ax[i,j].set_ylabel(r'$p(r)$')

plt.tight_layout()
plt.savefig('IFT/pr.png')
    
print('plot saved to IFT/pr.png')
plt.show()

