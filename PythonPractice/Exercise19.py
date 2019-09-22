def str_ret (str):
    substr = str[:2]
    if substr=="Is":
        return str;
    else:
        str1 = "Is" + str;
        return str1

print(str_ret("Is your house is nice ?"))
print(str_ret("your house is nice ?"))
print(str_ret("y"))