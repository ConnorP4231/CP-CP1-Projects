# Connor Pavicic, shoppingList

my_list = []

def add(add_item):
    my_list.append(add_item)
    return my_list

def remove(remove_item):
    if remove_item in my_list:
        my_list.remove(remove_item)
    else:
        print("Item not found in list.")
    return my_list

while True:
    action = input("""What would you like to do?
Enter 1 to add item
Enter 2 to remove item
Enter 3 to leave the list:\n""")

    if action == "1":
        add_item = input("What item do you want to add?: ")
        print(add(add_item))
    elif action == "2":
        remove_item = input("What item do you want to remove?: ")
        print(remove(remove_item))
    elif action == "3":
        print("Ok bye.")
        break
    else:
        print("Invalid option. Please try again.")