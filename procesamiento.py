import numpy as np
import sounddevice as sd
from scipy.fft import fft, fftfreq

def capturar_y_procesar_audio(duracion=3.0, frecuencia_base=44100):
    muestras = int(frecuencia_base * duracion)

    # Grabación del audio
    audio = sd.rec(muestras, samplerate=frecuencia_base, channels=1)
    sd.wait()

    # Dominio del tiempo
    tiempo = np.linspace(0.0, duracion, muestras)

    # Centrar señal (eliminar componente DC) y FFT
    audio_centrado = audio[:, 0] - np.mean(audio[:, 0])
    fourier = fft(audio_centrado)
    frecuencias = fftfreq(muestras, 1.0 / frecuencia_base)

    mitad = muestras // 2
    eje_frecuencias = frecuencias[:mitad]
    magnitud = np.abs(fourier[:mitad]) / muestras

    # Frecuencia fundamental
    indice_inicio = np.argmax(eje_frecuencias >= 50.0)
    posicion_relativa = np.argmax(magnitud[indice_inicio:])
    posicion_maxima = indice_inicio + posicion_relativa
    frecuencia_dominante = eje_frecuencias[posicion_maxima]

    # Retorno de datos en forma de diccionario
    return {
        "tiempo": tiempo,
        "audio": audio,
        "eje_frecuencias": eje_frecuencias,
        "magnitud": magnitud,
        "frecuencia_dominante": frecuencia_dominante
    }