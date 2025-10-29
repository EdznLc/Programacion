
import tkinter as tk

window = tk.Tk()
window.title("Uso de frames")
window.geometry("800x600")

frame = tk.Frame(window, width=300, height=200, bg="red", border=5, relief="solid")
frame.pack_propagate(False)
frame.pack(padx=50, pady=20)

frame2 = tk.Frame(frame, width=200, height=100, bg="cyan", border=2, relief="groove")
frame2.pack(padx=50, pady=50)

window.mainloop()