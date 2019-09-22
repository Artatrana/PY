def sum_thrice(x, y, z):
    sum = x+y+z
    if x==y==z :
        return sum * 3
    else:
        return sum
        
print(sum_thrice(1,2,3))
print(sum_thrice(3,3,3))

