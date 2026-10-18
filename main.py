#Recoleccion de los datos de amplitud y tiempo
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
plt.show()