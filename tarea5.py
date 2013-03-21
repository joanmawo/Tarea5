import sys
import os
import pylab
import numpy as np
import scipy
from scipy.linalg import eigh
#from scipy.optimize import curve_fit
from scipy.fftpack import fft, fftfreq, ifft

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
pylab.savefig("Manchas")
pylab.show()

fft_x = fft(NumeroManchas) #/len(Tiempo) # FFT Normalized
freq = fftfreq(len(Tiempo), 1.0/12.0) # Recuperamos las frecuencias
fft_x2 = fft(NumeroManchas) #/len(Tiempo) #Para el punto 5to
pylab.plot(freq,np.abs(fft_x))



#Calcula el cuadrado de las potencias y prepara la grafica de estas versus la frecuencia

potencias = np.abs(fft_x)**2
pylab.plot(freq, potencias, '.')
pylab.xlabel('Frecuencias')
pylab.ylabel('Potencia')
pylab.title('Frecuencias vs Potencia')
pylab.savefig("Potencia")
pylab.show()


#Crea una tabla que solo incluye las potencias de frecuecias entre 1 y 20 anios
tabla1=[]
tabla2=[]

for i in range(len(freq)):
	if (freq[i]!=0.0):
		peri=1/freq[i]
		if (peri>=1.0 and peri<=20.0):
			tabla1.append(peri)
			tabla2.append(potencias[i])

pylab.plot(tabla1, tabla2, '.')
pylab.xlabel('Periodo (Anios)')
pylab.ylabel('Potencia')
pylab.title('Periodo vs Potencia')
pylab.savefig("Periodo")
pylab.show()
	

#Filtra las frecuencias
for i in range(len(freq)):
	if (freq[i]>=1.0/20.0): #Creo que la frecuencia debe ser menor a 1/20
		fft_x2[i]=0.0 
	if (freq[i]<=-1.0/20.0):
		fft_x2[i]=0.0

Inv_limpia= ifft(fft_x2)
Inv_limpia_real = np.real(Inv_limpia)

#Grafica el numero de manchas y la funcion ajustada contra el tiempo
pylab.plot(Tiempo, NumeroManchas, '.')
pylab.plot(Tiempo, Inv_limpia_real, linewidth=5, alpha = 0.5)
pylab.xlabel('Tiempo (anios)')
pylab.ylabel('Promedio de manchas solares')
pylab.title('Promedio de manchas solares vs tiempo ')
pylab.savefig("Ajuste")
pylab.show()

#Se ve que en la grafica de la potencia al cuadrado para periodos entre 1 y 20 anios el maximo esta en 11.1085 anios. Esto indica que el periodo del ciclo solar esta alrededor de este valor. La curva de ajuste del ciclo solar muestra un maximo en 1985. Los siguientes maximos solares ocurriran cada 11.1085 anios a partir de este.

#Calculo del proximo maximo solar
anio_actual = 2013
anio = 1985
periodo_solar = 11.1085
encontrado = False

maximos_solares_rango = []
rango = 10
i = 1

while (encontrado == False):
	anio = anio + periodo_solar	
	if (anio >= anio_actual):
		encontrado = True

while(i < rango):
	temp = anio + i*periodo_solar
	maximos_solares_rango.append(temp)
	i += 1

print "El maximo solar siguiente sera en el "
print anio

#print "Los 10 siguientes maximos solares ocurriran en "
#print maximos_solares_rango




