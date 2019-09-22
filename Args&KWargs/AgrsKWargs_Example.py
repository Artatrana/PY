#Python Example to check Agrs and KWargs
def foo(required, *args, **kwagrs):
	print(required)
	if args:
		print(args)
	if kwagrs:
		print(kwagrs)

#foo()
#foo('hello')

foo('hello',1,2,4)
foo('hello',1,2,4,3,4,5,6)

foo('hello', key1 = 1, key2=2, key3=3)

foo('hello', 1,2,4,3,key1 = 1, key2=2, key3=3)
