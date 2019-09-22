# Sri Vishnu Sahasranamam & Meaning

from PIL import Image, ImageTk
import tkinter.font as tkFont
import pandas as pd  
from pandas import ExcelWriter
from pandas import ExcelFile
import tkinter as tk
import time

window = tk.Tk()
window.geometry("570x500")
window.title("Sri Vishnu Sahasranamam and Meaning")



image = Image.open('C:\Biju\PersonalDoc\Vishnu.jpg')
image.thumbnail((400,400),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)


customFont = tkFont.Font(family="Helvetica", size=12)
lableFont = tkFont.Font(family="Helvetica", size=16,weight="bold")

label_sloka = tk.Label(text="Sloka",background="black", foreground="yellow",  font=customFont)
label_sloka.grid(column=1, row=1)

text_sloka = tk.Text(master=window, height=5, width=62,background="black", foreground="green",  font=customFont)
text_sloka.grid(column=1, row=2)
#text_sloka.tag_config("here", background="black", foreground="green")
sloka_text = '''Om SuklAmbara-dharam vishNum SaSivarnam catur-bhujam
prasanna-vadanam dhyAyet sarva-vighnopaSAntaye.'''
#text_sloka.insert(tk.END,sloka_text) #commented to display the by looping

label_meaning = tk.Label(text="Meaning",background="black", foreground="yellow",  font=customFont)
label_meaning.grid(column=1, row=3)

text_meaning = tk.Text(master=window, height=10, width=62,background="black", foreground="green", font=customFont)
text_meaning.grid(column=1, row=4)
meanig_text = '''(For the eradication of all obstructions) One should meditate upon vishNu 
Who is clad in white robes, Who has a moonlike lustre, Who has four arms and 
Who has a beneficient face.'''
#text_meaning.insert(tk.END,meanig_text) #commented to display the by looping

data = pd.read_excel("C:\Biju\PersonalDoc\ishnu_SahasraNamaMeaning.xlsx")

#def refresher():
for index, row in data.iterrows():
	text_sloka.insert(tk.END, row['Sloka'])
	text_meaning.insert(tk.END, row['Meaning'])
	time.sleep(1)

	
window.mainloop()