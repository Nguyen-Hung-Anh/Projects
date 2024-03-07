# Function to read athlete records from a file into a dictionary
# This lab serves as an introduction to using exceptions. 
# You will modify an existing program to make it more robust by handling several possible errors.

def read_records_file(fname):
    '''
    Returns empty dictionary if the file doesn't exist or is empty.
    '''
    prs = {}  # Using a dictionary to store athlete records
    
    try:
        f = open(fname, 'r')  # Open the file in read mode
        line = f.readline()

        # Read each line, split it into parts, and store in the dictionary
        while line:
            line_parts = line.strip().split(',')
            prs[line_parts[0]] = int(line_parts[1])
            line = f.readline()

        f.close()  # Close the file
    except FileNotFoundError:
        print(f"File '{fname}' not found.")
    except IndexError:
        print(f"Error reading line in '{fname}'.")
    except ValueError:
        print(f"Error converting string to integer in '{fname}'.")
    
    return prs

# Function to write athlete records from a dictionary to a file
def write_records_file(fname, prs):
    '''
    Writes the dictionary prs to a text file named by the string fname.
    '''
    try:
        f = open(fname, 'w')  # Open the file in write mode
        for name in prs:
            output_line = name + ',' + str(prs[name]) + '\n'
            f.write(output_line)  # Write each record to the file
    except IOError:
        print(f"Error writing to file '{fname}'.")
    finally:
        f.close()  # Ensure the file is closed

# Function to insert a new athlete record
def insert_athlete(fname):
    athlete_name = input('Who are we adding? ')
    
    try:
        height = int(input(f'How high did {athlete_name} jump? '))
    except ValueError:
        print("Invalid input. Height must be an integer.")
        return

    prs = read_records_file(fname)
    if athlete_name in prs:
        print(f'An athlete by the name {athlete_name} already exists.\n\
                Choose another name, or use menu option 3 to update their information.')
    else:
        prs[athlete_name] = height
        print(f'{athlete_name} insert successfully.')
        write_records_file(fname, prs)

# Function to remove an athlete record
def remove_athlete(fname):
    athlete_name = input('Who are we removing? ')
    prs = read_records_file(fname)

    try:
        del prs[athlete_name]
        print(f'{athlete_name} removed successfully.')
        write_records_file(fname, prs)
    except KeyError:
        print(f'{athlete_name} not found.')

# Function to update an athlete record
def update_athlete(fname):
    athlete_name = input('Who are we updating? ')
    prs = read_records_file(fname)
    if athlete_name in prs:
        try:
            height = int(input(f'How high did {athlete_name} jump? '))
        except ValueError:
            print("Invalid input. Height must be an integer.")
            return
        
        if height > prs[athlete_name]:
            prs[athlete_name] = height
            print(f'{athlete_name} update successfully.')
            write_records_file(fname, prs)
        else:
            print(f'{athlete_name}\'s PR was not updated, PR already {prs[athlete_name]} cm')

# Function to lookup an athlete's record
def lookup_athlete(fname):
    athlete_name = input('Who are we looking up? ')
    prs = read_records_file(fname)
    
    try:
        pr = prs[athlete_name]
        print(f"{athlete_name}'s PR is {pr} cm.")
    except KeyError:
        print(f'No athlete named {athlete_name}.')

# Function to print the menu options
def print_menu():
    print('1. Insert an athlete')
    print('2. Remove an athlete')
    print('3. Update an athlete')
    print('4. Lookup an athlete')
    print('5. Quit this program')

# Main function to run the program
def main():
    QUIT_NUM = '5'
    records_file_name = 'high_jump.txt'
    
    print_menu()
    menu_option = input('What would you like to do? ')

    while menu_option != QUIT_NUM:
        if menu_option == '1':
            insert_athlete(records_file_name)
        elif menu_option == '2':
            remove_athlete(records_file_name)
        elif menu_option == '3':
            update_athlete(records_file_name)
        elif menu_option == '4':
            lookup_athlete(records_file_name)
        else:
            print('Sorry, that\'t not a valid option.')

        print_menu()
        menu_option = input('What would you like to do? ')

    print('Bye!')

if __name__ == '__main__':
    main()
