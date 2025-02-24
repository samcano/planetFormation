import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt
fl='HALLEY.clo'
sat_fl='SAT_HALLEY.clo'
jup_fl='JUP_HALLEY.clo'

data=open(fl,'r').readlines()
jupiter_encs=[x for x in data if 'JUPITER' in x]
saturn_encs=[x for x in data if 'SATURN' in x]
open(jup_fl,'w').writelines(jupiter_encs)
open(sat_fl,'w').writelines(saturn_encs)

data_j=np.loadtxt(jup_fl,usecols=(0,2))
data_s=np.loadtxt(sat_fl,usecols=(0,2))
os.remove(jup_fl)
os.remove(sat_fl)

fig=plt.figure()
plt.title('Halley Encounters with Giant Planets')
plt.xlabel('Time (years)')
plt.xlim(0,max(data_j[:,0])*1.1)
plt.ylim(0,max(data_j[:,1])*1.1)
plt.ylabel('$d_{enc}$ (au)')
plt.scatter(data_j[:,0],data_j[:,1],c='red',s=50,label='Jupiter')
plt.scatter(data_s[:,0],data_s[:,1],c='gold',s=50,label='SATURN')
plt.legend(loc='upper left')
plt.show()
fig.savefig('Halley_encounters.png')

