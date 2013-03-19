import sys
import os
import pylab
import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.optimize import curve_fit
from scipy.fftpack import fft, fftfreq

#datosFinales=open("data.dat", "w")

data=np.loadtxt('monthrg.dat')



Referencia=data[:,3]
NumeroManchas=[]
Tiempo = []
PromedioManchas=[]
AnioManchas=[]
ManchasMensuales=[]

for i in range(len(Referencia)):
	temp=data[i,0]
	if (temp>1795):
		Tiempo.append(data[i,0] + (1.0/12.0)*data[i,1])
		NumeroManchas.append(data[i,3])

pylab.plot(Tiempo, NumeroManchas, '.')
pylab.xlabel('Tiempo(anios)')
pylab.ylabel('Numero de Manchas')
pylab.title('Manchas vs Tiempo')
pylab.show()

fft_x = fft(NumeroManchas)/len(Tiempo) # FFT Normalized
freq = fftfreq(len(Tiempo), 1/12) # Recuperamos las frecuencias
pylab.plot(freq,np.abs(fft_x))

print freq

#Calcula el cuadrado de las potencias y prepara la grafica de estas versus la frecuencia

potencias = np.abs(fft_x)**2
pylab.plot(freq, potencias)

#Crea una tabla que solo incluye las potencias de frecuecias entre 1 y 20 anios
tabla1=[]
#for i
#for frecuencia in freq
#if (frecuencia > 1/20 and 1 > frecuencia)
#tabla.append(1/frecuencia, )

