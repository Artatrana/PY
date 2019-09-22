color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
color_list_3 = color_list_1 - color_list_2
print(color_list_3)
print(type(color_list_3))
print(color_list_1.difference(color_list_2))