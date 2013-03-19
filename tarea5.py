import sys
import os
import pylab
import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.optimize import curve_fit
from scipy.fftpack import fft, fftfreq


#datosFinales=open("data.dat", "w")

data=np.loadtxt(open("monthrg.dat", "r"))

print data

NumeroManchas=data[:,3]
Tiempo = data[:,0] + (1/12)*data[:,1] 

pylab.plot(Tiempo, NumeroManchas, '.')
pylab.xlabel('Tiempo(años)')
pylab.ylabel('Numero de Manchas')
pylab.title('Manchas vs Tiempo')
pylab.show()


fft_x = fft(NumeroManchas)/len(Tiempo) # FFT Normalized
freq = fftfreq(len(Tiempo), 1/12) # Recuperamos las frecuencias
pylab.plot(freq,np.abs(fft_x))
print freq

#Calcula el cuadrado de las potencias y prepara la gráfica de éstas versus la frecuencia
potencias = np.abs(fft_x)**2
pylab.plot(freq, potencias)

#Crea una tabla que sólo incluye las potencias de frecuecias entre 1 y 20 años
tabla1[]
for i 

for frecuencia in freq
	if (frecuencia > 1/20 and 1 > frecuencia)
	tabla.append(1/frecuencia, )
		
