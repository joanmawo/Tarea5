import sys
import os
import pylab
import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.optimize import curve_fit



#datosFinales=open("data.dat", "w")

data=np.loadtxt(open("monthrg.dat", "r"))

print data
#NumeroManchas=data[:,3]





