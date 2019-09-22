#create basic window

#TCL - Tools command lines

#Frame widgets : it like a widget holders.

import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text = 'test')
button = tk.Button(root, text = 'testbutton')

label.pack()
button.pack()


root.mainloop()