import tkinter as tk

window = tk.Tk()
window.title("Etiquetas")
window.geometry("800x600")

etiqueta1 = tk.Label(window)
etiqueta1.config(
    text="Este es el texto",
    height="2",
    bg="#FFDBF4"
)
etiqueta1.pack(pady=20)

marco1 = tk.Frame(window, bg="red", width=300, height=100)
marco1.propagate(False)
marco1.pack()

etiqueta2 = tk.Label(marco1, text="Soy una label", bg="red")
etiqueta2.pack(anchor="center", pady=10)

window.mainloop()