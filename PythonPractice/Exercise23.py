#Python program to get n copy of first 2 character of the string
str1 = input("Please input the string :")
n = int(input("Please enter the value of n :"))

outstr =''
strlength = len(str1)
if strlength > 2:
    substr = str1[:2]
else:
    substr = str1

for rec in range(n):
        outstr = outstr + substr
print(outstr)
        