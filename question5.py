#!/usr/bin/python3
"""
Name: Chisenga Musungaila
ID : 162314
"""
import numpy as np
import matplotlib.pyplot as pl
#Assign parameters, constants, step-time and initial values
#Assign here
g = 9.8
m = 2
tfinal = 100
dt = 1.0
Bnodrag = 0
B = 0.026
X0 = 0
Y0 = 0
V0 = 700
#initialize arrays
t = np.arange(0.,tfinal+dt,dt)
npoints = len(t)
Xnodrag = np.zeros(npoints)
Ynodrag = np.zeros(npoints)
VYnodrag = np.zeros(npoints)
VXnodrag = np.zeros(npoints)
VYdrag = np.zeros(npoints)
Ydrag = np.zeros(npoints)
Xdrag = np.zeros(npoints)
VY = np.zeros(npoints)
#Exact solution
H = Y0+V0*t-0.5*g*t**2
#Initial values for arrays. Euler's method, no drag solution
Xnodrag[0] = X0
VYnodrag[0] = V0
for i in range(npoints-1):
    Xnodrag[i+1] = Xnodrag[i] + VYnodrag[i]*dt
    VYnodrag[i+1] = VYnodrag[i] - (g+Bnodrag/m*Xnodrag[i])*dt
    Ynodrag[i+1] = Xnodrag[i+1] - VYnodrag[i+1] * dt
#Initial values for arrays. Euler's method, drag solution
Xdrag[0]= X0
VYdrag[0]= V0
 
for i in range(npoints-1):
    Xdrag[i+1]= Xdrag[i] + VYdrag[i]*dt
    VYdrag[i+1]= VYdrag[i] - (g+B/m*Xdrag[i]) * dt
    Ydrag[i+1]= Xdrag[i+1] - VYdrag[i+1] *dt  
    
# Plot results
pl.ion()
pl.plot(t,Ynodrag,'b',label='No drag')
pl.plot(t,Ydrag,'g',label='Non-zero drag')
pl.plot(t,H,'r',label='exact') 
pl.xlabel('time (s)')
pl.ylabel('displacement (m)')
pl.legend(loc=2, bbox_to_anchor=(0.45,1.0))
pl.show()
pl.savefig("question5.png") 
    