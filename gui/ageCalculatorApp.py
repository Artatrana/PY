#Create a person Class and create the init methon having name and birth_date
from PIL import Image, ImageTk

import datetime
import math
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
window.title("Age Calculator App")

year_label = tk.Label(text ="Year")
year_label.grid(column=0, row =1)

month_label = tk.Label(text ="Month")
month_label.grid(column=0, row =2)

day_label = tk.Label(text ="Day")
day_label.grid(column=0, row =3)

year_entry = tk.Entry()
year_entry.grid(column=1, row =1)

month_entry = tk.Entry()
month_entry.grid(column=1, row =2)

day_entry = tk.Entry()
day_entry.grid(column=1, row =3)

def calculate_age():
	print(year_entry.get())
	print(month_entry.get())
	print(day_entry.get())
	print("Button was clicked")

	arta = Person('Artatrana',datetime.date(int(year_entry.get()),int(month_entry.get()),int(day_entry.get())))
	print(arta.name)

	text_answer = tk.Text(master=window, height=20, width=30)
	text_answer.grid(column=1, row=5)
	answer_text = '{name} is {age} years old'.format(name=arta.name, age= arta.age())
	text_answer.insert(tk.END,answer_text)


calculate_button = tk.Button(text="Calculate Now", command=calculate_age)
calculate_button.grid(column=1, row =4)


class Person(object):
	"""docstring for person"""
	def __init__(self, name, birthdate):
		self.name = name
		self.birthdate = birthdate

	#This will not return the right age
	def age(self):
		today = datetime.date.today()
		#age = today.year - self.birthdate.year
		age = ((today-self.birthdate).days/365)

		return math.floor(age)

image = Image.open('C:\Biju\PersonalDoc\MyPic.jpg')
image.thumbnail((100,100),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)

#defining a object
#arta = Person('Artatrana',datetime.date(1977, 8,13))

#print(arta.name)
#print(arta.birthdate)	
#print(arta.age())	

window.mainloop()
