import numpy as np
from os.path import exists
import matplotlib.pyplot as plt

def plot_results(q,I,dI,func,pfit,*popt):
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
 
    # plot data and fit(s) 
    f,(ax0,ax1) = plt.subplots(2,1,gridspec_kw={'height_ratios': [4,1]})
    ax0.errorbar(q,I,yerr=dI,linestyle='none',marker='.',color='red',label='Data',zorder=0)
    ax0.plot(qfit_plot,Ifit_plot,color='black',label='New fit, chi2r = %1.1f' % chi2r,zorder=1)

    # import and plot previous fit
    file_prev = 'Ifit.dat'
    if exists(file_prev):
        qfit_prev,Ifit_prev = np.genfromtxt(file_prev,skip_header=2,usecols=[0,1],unpack=True)
        ax0.plot(qfit_prev,Ifit_prev,linestyle='--',color='darkviolet',label='Previous fit',zorder=2)

    # plot residuals
    ax1.plot(q,R,linestyle='none',marker='.',color='red')
    ax1.plot(q,q*0,color='black')
    
    # plot settings
    ax0.set_xscale('log')
    ax0.set_yscale('log')
    ax0.set_ylabel('Intensity')
    ax0.set_xticks([])
    ax0.legend(frameon=False)
     
    Rmax = np.ceil(np.amax(abs(R)))
    ax1.set_ylim(-Rmax,Rmax)
    ax1.set_yticks([-Rmax,0,Rmax])
    ax1.set_xlabel(r'$q$')
    ax1.set_ylabel(r'$\Delta I/\sigma$')
    ax1.set_xscale('log')

    plt.show()
