import tkinter as tk

window = tk.Tk()

window.geometry("800x500")
window.title("GG")

label = tk.Label(window, text="Hello", font=('Arial', 18))
label.pack(padx=20, pady= 20)

list = tk.Text(window, height=2, font=('Arial', 16))
list.pack(padx = 10)

buttonFrame = tk.Frame(window)
buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0)


window.mainloop()
