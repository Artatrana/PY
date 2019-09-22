import tkinter as tk

def doorbell(event):
    print("You rang the doorbell!!!")

window = tk.Tk()
window.geometry("1000x700")

alabel = tk.Label(text="Banana")
alabel.grid(column=0, row=0)

alabel2 = tk.Label(text="Apple")
alabel2.grid(column=1, row=0)

button = tk.Button(window, text="Doorbell")
button.grid(column=0)

button2 = tk.Button(window, text="10")
button2.grid(column=1, row=1)

button.bind("<Button-1>",doorbell)

window.mainloop()