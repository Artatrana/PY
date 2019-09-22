#Python program to count 4 in the list
counter = 0
list_number = [1,3,5,4, 5,55,6,44,55]
for item in list_number:
    if item == 4:
        counter += 1

print("Number of 4 in the list is ", counter)