def fun1(input_num):
    if input_num > 17:
        return (abs(17-input_num)*2)
    else:
        return(17-input_num)
        

input_num = int(input("Please input the number :"))
print(fun1(input_num))
 