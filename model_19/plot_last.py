import numpy as np
import matplotlib.pyplot as plt

q,I,dI    = np.genfromtxt('Idat.dat',skip_header=1,usecols=[0,1,2],unpack=True)
qfit,Ifit = np.genfromtxt('Ifit.dat',skip_header=1,usecols=[0,1],unpack=True)
    
# plot data and fit(s) 
plt.errorbar(q,I,yerr=dI,linestyle='none',marker='.',color='red',label='Data',zorder=0)
plt.plot(qfit,Ifit,color='black',label='New fit',zorder=1)
    
# plot settings
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$q$')
plt.ylabel('Intensity')
plt.legend()
plt.show()
