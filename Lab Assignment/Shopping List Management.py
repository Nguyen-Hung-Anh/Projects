'''
Shopping_list_management.py -- Nguyen Hung Anh -- 10/16/2023

# This program manages a digital shopping list with the following functions:
#   - add_item(item_list, checked_items_list): Adds an item to the list.
#   - remove_item(item_list, checked_items_list): Removes an item from the list.
#   - check_off_item(item_list, checked_items_list): Checks off an item on the list.
#   - uncheck_item(item_list, checked_items_list): Unchecks an item on the list.
#   - display_list(item_list, checked_items_list): Displays the current shopping list.
# The main() function allows the user to interactively modify the list until they choose to quit (press "q").
# The two lists, item_list and checked_items_list, are modified in place.
# Example usage is provided to demonstrate the program's functionality.
'''

def add_item(item_list, checked_items_list):
    print()
    s_user = input("Item to add: ")
    item_list.append(s_user)
    checked_items_list.append(False)
    print(s_user, "added.")
    print()

def remove_item(item_list, checked_items_list):
    print()
    s_user = input("Item to remove: ")
    for i in range(len(item_list)):
        if s_user == item_list[i]:
            item_list.remove(s_user)
            del checked_items_list[i]
        else:
            print("Invalid Input")
    
def check_off_item(item_list, checked_items_list):
    s_user = input("Item to check off: ")
    for i in range(len(item_list)):
        if s_user == item_list[i]:
            checked_items_list[i] = True
        else:
            print("Invalid Input")
            
def uncheck_item(item_list, checked_items_list):
    s_user = input("Item to uncheck: ")
    for i in range(len(item_list)):
        if s_user == item_list[i]:
            checked_items_list[i] = False
        else:
            print("Invalid Input")

def display_list(item_list, checked_items_list):
    for i in range(len(item_list)):
        if checked_items_list[i]:
            checkbox = "[X]"
        else:
            checkbox = "[ ]"
        print(f"{checkbox} {item_list[i]}")
        
  
def main():
    item_list = []
    checked_items_list = []

    while True:
        print("[A]dd", "[C]heck off", "[U]ncheck item", "[D]isplay list", "[R]emove", "[Q]uit", sep = "\n")
        print()
        s_user = input("Select an option: ").lower()
        while s_user != 'a' and s_user != 'c' and s_user != 'u' and s_user != 'd' and s_user != 'r' and s_user != 'q':
            s_user = input("Select an option:")
        if s_user == 'a':
            add_item(item_list, checked_items_list)
        elif s_user == 'c':
            check_off_item(item_list, checked_items_list)
        elif s_user == 'u':
            uncheck_item(item_list, checked_items_list)
        elif s_user == 'd':
            display_list(item_list, checked_items_list)
        elif s_user == 'r':
            remove_item(item_list, checked_items_list)
        else:
            break
        
if __name__ == "__main__":
    main()
