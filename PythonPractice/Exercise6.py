test_list=[]
test_tuple = ()

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    test_list.append(num)
    test_tuple= tuple(test_list)
    
print( 'list', test_list)
print( 'Tuple', test_tuple)
#print("Tuple of number is "+ test_tuple)   
    