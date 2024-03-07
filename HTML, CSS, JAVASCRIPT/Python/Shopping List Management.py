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

# Function to add an item to the shopping list
def add_item(item_list, checked_items_list):
    print()
    # Ask user for the item to add
    s_user = input("Item to add: ")
    # Add the item to the item list
    item_list.append(s_user)
    # Add a corresponding unchecked item to the checked items list
    checked_items_list.append(False)
    print(s_user, "added.")
    print()

# Function to remove an item from the shopping list
def remove_item(item_list, checked_items_list):
    print()
    # Ask user for the item to remove
    s_user = input("Item to remove: ")
    # Iterate through the item list
    for i in range(len(item_list)):
        # If the item matches, remove it from both lists
        if s_user == item_list[i]:
            item_list.remove(s_user)
            del checked_items_list[i]
        else:
            print("Invalid Input")

# Function to check off an item on the shopping list
def check_off_item(item_list, checked_items_list):
    s_user = input("Item to check off: ")
    # Iterate through the item list
    for i in range(len(item_list)):
        # If the item matches, mark it as checked
        if s_user == item_list[i]:
            checked_items_list[i] = True
        else:
            print("Invalid Input")

# Function to uncheck an item on the shopping list
def uncheck_item(item_list, checked_items_list):
    s_user = input("Item to uncheck: ")
    # Iterate through the item list
    for i in range(len(item_list)):
        # If the item matches, mark it as unchecked
        if s_user == item_list[i]:
            checked_items_list[i] = False
        else:
            print("Invalid Input")

# Function to display the current shopping list
def display_list(item_list, checked_items_list):
    for i in range(len(item_list)):
        # Display the item along with its check status
        if checked_items_list[i]:
            checkbox = "[X]"
        else:
            checkbox = "[ ]"
        print(f"{checkbox} {item_list[i]}")

# Main function to interactively manage the shopping list
def main():
    item_list = []
    checked_items_list = []

    while True:
        # Print menu options
        print("[A]dd", "[C]heck off", "[U]ncheck item", "[D]isplay list", "[R]emove", "[Q]uit", sep="\n")
        print()
        # Ask user to select an option
        s_user = input("Select an option: ").lower()
        # Validate user input
        while s_user not in ['a', 'c', 'u', 'd', 'r', 'q']:
            s_user = input("Select an option:")
        # Execute corresponding function based on user input
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
            # Exit loop if user chooses to quit
            break

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()