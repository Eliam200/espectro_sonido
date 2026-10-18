#Captura de audio
import numpy as np
import sounddevice as sd

frecuencia_base = 44100
duracion = 3.0
muestras = int(frecuencia_base*duracion)

print("Grabando sonido...")

audio = sd.rec(muestras,samplerate=frecuencia_base,channels=1)
sd.wait()

print("Grabacion finalizada.")

print(audio.shape)

tiempo = np.linspace(0.0,duracion,muestras)
print(tiempo)

#Visualizacion de los datos recopilados
import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))
plt.plot(tiempo,audio)
plt.xlabel("Tiempo(s)")
plt.ylabel("Amplitud")
plt.title("Gráfica de Amplitud vs Tiempo")
plt.grid(True)

#Transformada de Fourier
from scipy.fft import fft, fftfreq

audio_centrado = audio[:,0] - np.mean(audio[:,0])

fourier = fft(audio_centrado)
frecuencias = fftfreq(muestras,1.0/frecuencia_base)

mitad = muestras//2

eje_frecuencias = frecuencias[:mitad]
magnitud = np.abs(fourier[:mitad]) / muestras

#Grafica de espectro de frecuencias     
plt.figure(figsize=(10,4))
plt.plot(eje_frecuencias,magnitud)
plt.xlabel("Frecuencia(Hz)")
plt.ylabel("Amplitud")
plt.title("Espectro de frecuencias")
plt.grid(True)
plt.xlim(10,2000)

plt.show()

#Calculo del pico mas alto de frecuencia

posicion_maxima = np.argmax(magnitud)
frecuencia_max = eje_frecuencias[posicion_maxima]
print(f"El pico mas alto de frecuencia es: {frecuencia_max}")