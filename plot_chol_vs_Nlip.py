import numpy as np
import matplotlib.pyplot as plt

## figure settings
fig,ax = plt.subplots(1,2,figsize=(13,6))
p0 = ax[0].twinx()
p1 = ax[1].twinx()


## Number of lips vs poly/lip ratio
elements = [\
['POPC',[2,4],[40.1,17.0],'skyblue','blue',[4.27,3.49]],\
['DMPC',[0.5,1.0,2.0],[96.6,74.9,42.8],'pink','red',[5.06,4.50,3.83]]]

for element in elements:
    name  = element[0]
    Ratio = element[1]
    Nlip  = element[2]
    color = element[3]
    color2 = element[4]
    Radius = element[5]

    ax[0].plot(Ratio,Nlip,linestyle='none',marker='s',markersize=9,color=color,label='Number of lipids, %s' % name)
    p0.plot(Ratio,Radius,linestyle='none',marker='x',markersize=6,color=color2,label='Average radius, %s' % name)

ax[0].plot([0,5],[15,15],linestyle='--',color='grey',label='estimate of phase transition')
#ax[0].plot([0,5],[15,15],linestyle='--',color='grey',label='estimate of phase transition, discoidal -> spherical lipid particle')
ax[0].set_xlabel('Polymer/lipid ratio, R')
ax[0].set_ylabel('Number of lipids')
ax[0].set_ylim(0,100)
ax[0].set_xlim(0,5)
ax[0].text(2.0,70,'0 mol%s Chol' % '%')
#ax[0].legend(loc='upper center',bbox_to_anchor=(1.1,1.1),fancybox=True,shadow=True,ncol=5)
ax[0].legend(loc='upper left',bbox_to_anchor=(1.2,.5),prop={'size':10},frameon=False)
p0.legend(loc='upper left',bbox_to_anchor=(1.2,.38),prop={'size':10},frameon=False)

R_lim = [3.,5.15]
R_ylabel = 'Radius [nm]'
p0.set_ylabel(R_ylabel)
p0.set_ylim(R_lim)

## Number of lips vs chol
elements = [\
#['POPC',[0,10,20,20],[17.1,13.8,5.5,5.7],'skyblue','blue',4,[34.9,34.3,30.4,31.9]],\
['POPC',[0,8,18,15],[17.0,13.8,5.6,5.9],'skyblue','blue',4,[3.49,3.43,3.04,3.20]],\
['DMPC',[0,1.4,1.4,3.3],[42.8,33.4,28.7,6.2],'pink','red',2,[3.83,3.63,3.67,3.10]]]

for element in elements:
    name  = element[0]
    chol  = element[1]
    Nlip  = element[2]
    color = element[3]
    color2 = element[4]
    #Ratio = element[5]
    Radius= element[6]

    ax[1].plot(chol,Nlip,linestyle='none',marker='s',markersize=9,color=color,label='Number of lipids, %s' % name)
    p1.plot(chol,Radius,linestyle='none',marker='x',markersize=6,color=color2,label='Average radius, %s' % name)

PT = 15 # estimate of phase transition
ax[1].plot([-1,21],[PT,PT],linestyle='--',color='grey',label='estimate of phase transition, discoidal -> spherical lipid particle')    
ax[1].set_xlabel('mol%s cholesterol' % '%')
ax[1].set_ylabel('Number of lipids')
ax[1].set_ylim(0,100)
ax[1].set_xlim(-1,21)
ax[1].text(3.5,70,'R=4 for POPC, R=2 for DMPC')

p1.set_ylabel(R_ylabel)
p1.set_ylim(R_lim)

plt.tight_layout()
plt.savefig('output/Nlip.png')
plt.show()

