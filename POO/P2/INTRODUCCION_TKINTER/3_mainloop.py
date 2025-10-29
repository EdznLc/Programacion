import tkinter as tk

window = tk.Tk()

window.title("Mainloop")
window.geometry("800x600")
window.resizable(False, False)

frame = tk.Frame(window)
frame.config(
    width=600,
    height=400,
    bg="#0ae4f0",
    bd=10,
    relief="raised")
frame.pack(pady=10, padx= 10, anchor="n")

window.mainloop()