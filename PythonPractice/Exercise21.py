#Python program to find given number is odd or even
def odd_even(n):
    if n%2 == 1:
        type ="odd"
        
    else:
        type = "even"
    return type

print(odd_even(5) )
print(odd_even(6) )