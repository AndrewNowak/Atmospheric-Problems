#6/27/22
#Author: Andrew Nowak

# Analysis of a very simple "glass plane" atmosphere model. The model calculates the energy balance, and thus the temperature,
#for the atmosphere as a function of the atmospheric layer. The assumption is the atmposhere is transparent to solar radiation but 
#a perfectly efficient absorber/emitter of ground radiation. The model also assumes only one emssion/ one absorbtion of radiation.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

L= 1350
alpha = 0.3
sunEmiss = L*(1-alpha)/4

epsilon = 1
sigma = 5.67e-8

numAtmLayers = 1
layer = np.linspace(0,numAtmLayers,numAtmLayers+1)
print(layer)

#the ground
def GrndBalance(T):
    return L*(1-alpha)/4 - epsilon*sigma*(T**4)

root = fsolve(GrndBalance,[100,500])

T=np.zeros(numAtmLayers+1)
T[0] = root[0]

#the atmosphere
def EnergyBalance(T):
    return energyIN - 2*epsilon*sigma*(T**4) 

for i in range(numAtmLayers):
    energyIN = epsilon*sigma*(T[i]**4) 
    root = fsolve(EnergyBalance,[0,260])
    if root[0] >= 0:
        T[i+1] = root[0]
    else:
        T[i+1] = root[1]

print(T)

plt.figure(1)
plt.plot(T,layer,'r-')
plt.title('A very simple model of atmospheric energy balance')
plt.ylabel('layer')
plt.xlabel('Temperature (K)')
plt.grid()
plt.show()
