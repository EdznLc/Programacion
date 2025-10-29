"""
Tkinter trabaja a traves de interfaces, es una biblioteca de Python que permite crear aplicaciones en python para escritorio.
"""

import tkinter as tk

window = tk.Tk()
window.title("Mi primera App Grafica en Tkinter con Python")
window.geometry("1000x600")
window.resizable(False, False)

window.configure(
    background="#123456"
    )

window.mainloop()