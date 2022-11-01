import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import os

def interp(x_in,y_in,x_out):
    f = interpolate.interp1d(x_in,y_in)
    y_out = f(x_out)

    return y_out

SHOW_PLOT = 1

colors = ['dodgerblue','turquoise','mediumseagreen','y','orange','red']
#colors = ['royalblue','cyan','limegreen','y','orange','red']
dataset = [\
[1, '154_J1_POPC_R2',        'POPC', '2',   0, 0, 0, 1e1,colors[0]],\
[2, '154_J2_POPC_R4',        'POPC', '4',   0, 0, 0, 1e0,colors[1]],\
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

print('\n')

for model in [11,19]:
#for model in range(1,21):
    model_folder = 'model_%s' % model

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
        data = '%s/%s/Idat.dat' % (model_folder,folder)
        fit = '%s/%s/Ifit.dat' % (model_folder,folder)
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
     
        ## normalize with I[0] (it's in arb units anyway)
        I,dI,Ifit = I/I[0],dI/I[0],Ifit/I[0]

        ## plot
        label = r'%s, %d%s Chol, $R$=%s, $\chi^2_r$ %1.1f' % (lipid,chol,'%',ratio,chi2r)
        ax[row,col].errorbar(q,I*scale,dI*scale,linestyle='none',marker='.',color=color,label = label,zorder=0)
        ax[row,col].plot(qfit,Ifit*scale,color='black',zorder=1)
        ax[row,col].legend(frameon=False,fontsize=9)

    for i in range(2):
        for j in range(2):
            ax[i,j].set_xscale('log')
            ax[i,j].set_yscale('log')
            ax[i,j].set_ylim(1e-2,1e3)
            ax[i,j].set_xlabel(r'$q$ [$\mathrm{\AA}^{-1}$]')
            ax[i,j].set_ylabel('I(q)/I(0) (scaled)')

    plt.tight_layout()
    plt.savefig('%s/all_fits' % model_folder)
    os.system('mkdir -p output')
    os.system('cp %s/all_fits.png output/model%s.png' % (model_folder,model))
    
    print('plot saved to output/model%s.png' % model)

    if SHOW_PLOT:
        plt.show()

print('\n')

