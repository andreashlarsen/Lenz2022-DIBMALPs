import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#data from:
# file:///Users/andreashlarsen/Downloads/jp310345j_si_001.pdf

temperature = np.linspace(35,60,6)
V_chol = [678.3,676.3,562,575.2,593.3,625.1]

plt.plot(temperature,V_chol,linestyle='none',marker='.',color='black',label='data')

def func(x,a,b):
    return a*x+b

popt,pcov = curve_fit(func,temperature,V_chol)

fit = func(temperature,*popt)

plt.plot(temperature,fit,color='black',label='fit')

plt.xlabel('temperature')
plt.ylabel('Volume cholesterol')

plt.show()
