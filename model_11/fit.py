import numpy as np
from scipy.optimize import curve_fit
from out import *

def fit(q,I,dI,func,pname,p0,pmin,pmax,pfit,tol):
    popt,pcov = curve_fit(func,q,I,sigma=dI,absolute_sigma=True,p0=p0,bounds=(pmin,pmax),xtol=tol,ftol=tol,verbose=2) #ftol and xtol default 1e-8
    Ifit = func(q,*popt)  
    perr = np.sqrt(np.diag(pcov))
                      
    for i in range(len(pname)):
        if pfit[i] == 0:
            out('%-16s: initial = %-10.5f (FIXED)' % (pname[i],popt[i]))
        elif popt[i] < pmin[i]+popt[i]*0.01 or popt[i] > pmax[i]-popt[i]*0.01:
            out('%-16s: initial = %-10.5f, min = %-10.5f, max = %-10.5f, fit =  %12.5f +/- %-11.5f !! fit value less than 1 prc from min or max of prior !!' % (pname[i],p0[i],pmin[i],pmax[i],popt[i],perr[i]))
        else:
            out('%-16s: initial = %-10.5f, min = %-10.5f, max = %-10.5f, fit =  %12.5f +/- %-11.5f' % (pname[i],p0[i],pmin[i],pmax[i],popt[i],perr[i]))
                      
    ## calculate chi2r    
    R = (Ifit - I)/dI        
    chi2 = np.sum(R**2)
    M = len(I)
    P = len(np.nonzero(pfit)[0])
    v = M - P # degrees of freedom 
    chi2r = chi2/v
    out('Chi2r = %4.2f' % chi2r)

    return(chi2r,*popt)
