import numpy as np
import matplotlib.pyplot as plt

def save_results(q,I,dI,func,pfit,*popt):
    qfit_plot = np.linspace(q[0],q[-1],2000)
    Ifit_plot = func(qfit_plot,*popt)
    
    ## calculate residuals   
    Ifit = func(q,*popt) 
    R = (Ifit - I)/dI     

    ## calculate chi2r   
    chi2 = np.sum(R**2)
    M = len(I)
    P = len(np.nonzero(pfit)[0])
    v = M - P # degrees of freedom 
    chi2r = chi2/v

    # write fit to file
    with open('Ifit.dat','w') as f:
        f.write('# q I_fit\n')
        f.write('# reduced chi-square = %1.2f\n' % chi2r)
        for x,y in zip(qfit_plot,Ifit_plot):
            f.write('%f %f\n' % (x,y))

    # write dat to file
    with open('Idat.dat','w') as f:
        f.write('# q I_dat dI_dat\n')
        for x,y,z in zip(q,I,dI):
            f.write('%f %f %f\n' % (x,y,z))

