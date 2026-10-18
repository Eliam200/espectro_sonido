import tkinter as tk 
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Análisis de espectro de sonido")
ventana.geometry("1000x600")

ttk.Button(ventana, text="Iniciar grabación")

ventana.mainloop