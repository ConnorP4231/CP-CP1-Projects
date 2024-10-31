def add_to_list(item, my_list = []):

     my_list.append(item)
     return my_list

     
while True:
     item = input("item: ")
     print(add_to_list(item))