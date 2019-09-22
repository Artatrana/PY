name = input("Please enter the first and last name :")
count = len(name)
new_name =''
while count > 0:
    new_name = new_name + name[count-1]
    count -= 1
print(new_name)
