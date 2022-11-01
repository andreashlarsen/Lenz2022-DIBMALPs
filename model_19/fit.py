import numpy as np
from scipy.optimize import curve_fit
from out import *

def fit(q,I,dI,func,pname,p0,pmin,pmax,pfit,tol):
    
    ## fit, get optimal params, popt and covariance of params, pvar
    popt,pcov = curve_fit(func,q,I,sigma=dI,absolute_sigma=True,p0=p0,bounds=(pmin,pmax),xtol=tol,ftol=tol,verbose=2) #ftol and xtol default 1e-8
    Ifit = func(q,*popt)  
    perr = np.sqrt(np.diag(pcov))
    N = len(pname)

    ## print covariance
    for i in range(N):
        for j in range(N):
            correlation = np.sqrt(np.abs(pcov[i,j]))
            magnitude = np.sqrt(np.abs(popt[i]*popt[j]))
            rel_cor = correlation/magnitude*100
            print('relative correlation between %-16s and %16s: %6.1f%s' % (pname[i],pname[j],rel_cor,'%'))
                      
    for i in range(N):
        if pfit[i] == 0:
            out('%-16s: initial = %-10.5f (FIXED)' % (pname[i],popt[i]))
        elif popt[i] < pmin[i]+popt[i]*0.01 or popt[i] > pmax[i]-popt[i]*0.01:
            prc = perr[i]/popt[i] * 100
            out('%-16s: initial = %-10.5f, min = %-10.5f, max = %-10.5f, fit =  %12.5f +/- %-11.5f (%-4.1f%s) !! fit value less than 1 prc from min or max of prior !!' % (pname[i],p0[i],pmin[i],pmax[i],popt[i],perr[i],prc,'%'))
        else:
            prc = perr[i]/popt[i] * 100
            out('%-16s: initial = %-10.5f, min = %-10.5f, max = %-10.5f, fit =  %12.5f +/- %-11.5f (%-4.1f%s)' % (pname[i],p0[i],pmin[i],pmax[i],popt[i],perr[i],prc,'%'))
                      
    ## calculate chi2r    
    R = (Ifit - I)/dI        
    chi2 = np.sum(R**2)
    M = len(I)
    P = len(np.nonzero(pfit)[0])
    v = M - P # degrees of freedom 
    chi2r = chi2/v
    out('Chi2r = %4.2f' % chi2r)

    return(chi2r,*popt)
