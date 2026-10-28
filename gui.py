import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from procesamiento import capturar_y_procesar_audio


def iniciar_interfaz():
    # Creación de la ventana
    ventana = tk.Tk()
    ventana.title("Analizador de Espectro Sonoro - Proyecto de Aula")
    ventana.geometry("1100x600")

    # Marco superior de controles
    marco_superior = ttk.Frame(ventana, padding=10)
    marco_superior.pack(side=tk.TOP, fill=tk.X)

    # Etiquetas
    etiqueta_estado = tk.Label(marco_superior, text="Estado: Listo", font=("Arial", 10, "bold"), fg="blue")
    etiqueta_estado.pack(side=tk.LEFT, padx=10)

    etiqueta_resultado = tk.Label(marco_superior, text="Frecuencia Fundamental: -- Hz", font=("Arial", 11, "bold"))
    etiqueta_resultado.pack(side=tk.RIGHT, padx=20)

    # Configuración de gráficas Matplotlib (lado a lado)
    fig, (ax_tiempo, ax_fft) = plt.subplots(1, 2, figsize=(10, 4.5))
    fig.tight_layout(pad=3.0)

    ax_tiempo.set_title("Amplitud vs Tiempo (En espera)")
    ax_tiempo.set_xlabel("Tiempo (s)")
    ax_tiempo.set_ylabel("Amplitud")
    ax_tiempo.grid(True)

    ax_fft.set_title("Espectro de Frecuencias (En espera)")
    ax_fft.set_xlabel("Frecuencia (Hz)")
    ax_fft.set_ylabel("Magnitud")
    ax_fft.grid(True)

    lienzo = FigureCanvasTkAgg(fig, master=ventana)
    lienzo.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Función que se ejecuta al presionar el botón
    def evento_boton():
        etiqueta_estado.config(text="Estado: 🔴 Grabando...", fg="red")
        ventana.update()

        # Llamamos a nuestro módulo externo de procesamiento
        datos = capturar_y_procesar_audio(duracion=3.0, frecuencia_base=44100)

        # Actualizamos la gráfica del tiempo
        ax_tiempo.clear()
        ax_tiempo.plot(datos["tiempo"], datos["audio"], color='#1f77b4')
        ax_tiempo.set_title("Gráfica de Amplitud vs Tiempo")
        ax_tiempo.set_xlabel("Tiempo (s)")
        ax_tiempo.set_ylabel("Amplitud")
        ax_tiempo.grid(True)

        # Actualizamos la gráfica de la FFT
        ax_fft.clear()
        ax_fft.plot(datos["eje_frecuencias"], datos["magnitud"], color='#ff7f0e')
        ax_fft.set_title("Espectro de Frecuencias (FFT)")
        ax_fft.set_xlabel("Frecuencia (Hz)")
        ax_fft.set_ylabel("Magnitud Normalizada")
        ax_fft.set_xlim(10, 2000)
        ax_fft.grid(True)

        lienzo.draw()

        etiqueta_estado.config(text="Estado: ✅ Análisis completado", fg="green")
        etiqueta_resultado.config(text=f"Frecuencia Fundamental: {datos['frecuencia_dominante']:.2f} Hz")

    # Botón de grabación conectado a la función interna
    boton_grabar = ttk.Button(marco_superior, text="🎤 Iniciar Grabación (3s)", command=evento_boton)
    boton_grabar.pack(side=tk.LEFT, padx=10)

    # Barra de herramientas de matplotlib para hacer zoom
    barra_herramientas = NavigationToolbar2Tk(lienzo, marco_superior)
    barra_herramientas.update()
    barra_herramientas.pack(side=tk.LEFT,padx=10)

    # Mantiene la ventana abierta
    ventana.mainloop()  