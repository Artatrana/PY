class Car():
	def __init__(self,color, milage):
		self.color = color
		self.milage = milage

class AlwaysBlueCar(Car):
	def __init__(self,*args, **kwagrs):
		super().__init__(*args, **kwagrs)
		self.color = 'blue'



