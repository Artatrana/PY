#print the extension of the file
filename = input("Please enter the file name")
pos = filename.find(".")
extn = filename[pos+1:]
print (extn)