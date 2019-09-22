#Python program to display the usefullness of args and kwargs
#if you want to do some kind of manipulation to args and kwargs
#to call another funciton from the main funciton

def foo(x, *args, **kwargs):
	#adding an extra element to kwargs
	kwargs['name']='Alice'

	#adding an extra element to args but since tupele is immutable we have
	#to create new agrs
	new_args=args + ('extra',)

	#calling anothe funciton with changed args and kwargs
	bar(x,*new_args,**kwargs)