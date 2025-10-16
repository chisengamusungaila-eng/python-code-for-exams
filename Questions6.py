#!/usr/bin/python3
import numpy as np
import math as m
import matplotlib.pyplot as pl
from numpy.random import RandomState
sig = 3.
mu = 0.
# make arrays of random numbers
r = RandomState()#assign RandomState() to r
n = 100000 #Set the number of random numbers to be generated
x = r.randn(n)*sig # normal distribution with standard deviation factor
x_r = np.linspace(-5.,5.)
XGausfunc = np.exp(-(x_r-mu)**2/(2.*sig**2))/(m.sqrt(2.*m.pi*sig**2))
pl.ion()
pl.plot(x_r,XGausfunc,'r',label='Gaussian function')
pl.figure(1) # simple histogram with 200 bins
pl.hist(x, bins=200,normed=True,label='Random-Normalized'); # Create histogram of 200 bins
pl.xlabel('Value')
pl.ylabel('Number')
pl.title('Normally Distributed Random Numbers')
pl.legend(loc=2, bbox_to_anchor=(0.45,1.0))
pl.savefig("question6.png")
pl.show()