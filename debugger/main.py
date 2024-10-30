def add_to_list(item, my_list = []):

     my_list.append(item)

     return my_list


item = input("What item do you want to add?: ")
item_2 = input("second item: ")
item_3 = input("third: ")

print(add_to_list(item))
print(add_to_list(item_2))
print(add_to_list(item_3))