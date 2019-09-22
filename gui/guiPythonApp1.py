#here we can add different app and Url to directly go to the 
#page from this APP

import tkinter as tk
import webbrowser

def doorbell(event):
    print("You rang the doorbell!!!")
    
def open_cp(event):
	webbrowser.open_new_tab("https://www.cleverprogrammer.com")
    #webbrowser.open_new_tab("https://www.w3resource.com/python-exercises/python-basic-exercises.php")
    #webbrowser.open_new_tab("https://www.codecademy.com")

def open_blog(event):
	webbrowser.open_new_tab("https://www.cleverprogrammer.com/blog")

window = tk.Tk()
window.geometry("600x400")

alabel = tk.Label(text="Banana")
alabel.grid(column=0, row=0)

alabel2 = tk.Label(text="Apple")
alabel2.grid(column=1, row=0)

alabel = tk.Label(text="Blog")
alabel.grid(column=2, row=0)

button = tk.Button(window, text="Doorbell")
button.grid(column=0)

button2 = tk.Button(window, text="Home")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="Blog")
button3.grid(column=2, row=1)


#binding to the left button of the mouse
button.bind("<Button-1>",doorbell)
button2.bind("<Button-1>",open_cp)
button3.bind("<Button-1>",open_blog)


window.mainloop()