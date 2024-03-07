# High-jump-records -- Nguyen Hung Anh -- 11/17/2023

def read_records_file(s_fname: str) -> dict:
    '''
    Reads a file named fname into a dictionary, with names as string keys,
    and PRs as integer values.
    '''
    records = {}
    file = open(s_fname, 'r')
    lines = file.readlines()
    for line in lines:
        name, pr = line.strip().split(",")
        records[name] = int(pr)
    file.close()
    return records
    pass

def write_records_file(s_fname: str, d_records: dict) -> None:
    '''Write d_records to a file named fname.'''
    file = open(s_fname, 'w')
    for name, pr in d_records.items():
        file.write(f'{name} {pr}\n')
    pass


def insert_athlete(d_records: dict, s_name: str, i_pr: int) -> None:
    '''
    Add a new person to the dictionary, unless they're already in it.
    If a name is already in the dict, prints a message about duplicate entries, 
    and does not update.
    '''
    if s_name not in d_records:
        d_records[s_name] = i_pr
    else:
        print(f'{s_name} already exists in the records.')
    pass


def remove_athlete(d_records: dict, s_name: str) -> None:
    '''
    Removes s_name from d_records. Prints an informational message 
    indicating success or failure.
    '''
    if s_name in d_records:
        del d_records[s_name]
        print(f' {s_name} has been removed from the record.')
    else:
        print(f' {s_name} not found in the records.')
    pass


def update_athlete(d_records: dict, s_name: str, i_pr: int) -> None:
    '''
    Updates the value for s_name in d_records. If the current value is higher than
    i_pr, the update is not made. If s_name is not in d_records, an informational 
    message is printed.
    '''
    if s_name in d_records:
        if i_pr > d_records[s_name]:
            d_records[s_name] = i_pr
        else:
            print(f'The current PR for {s_name} is higher than the provided PR. No update is made.')
    else:
        print(f'{s_name} not found in the records.')
    pass
    

def lookup_athlete(d_records: dict, s_name: str) -> None:
    '''
    Gets name input, prints the PR associated with it. If the name does not exist,
    an informational message is printed.
    '''
    if s_name in d_records:
        print(f'{s_name}\'s PR: {d_records[s_name]}')
    else:
        print(f'{s_name} not found in the records.')
    pass


def show_all_athletes(d_records: dict) -> None:
    '''
    Prints a nicely formatted list of two columns: names and PRs.
    The end of each name, and the end of each PR should line up.
    E.g.:
    Name    PR
    -------------
    James     123
    Ann        98
    Alfonso   201
    ...       ...

    '''
    print("Name\tPR")
    print("--------------")
    for name, pr in d_records.items():
        print(f"{name}\t{pr}")
    pass

def print_menu():
    print('1. Insert an athlete')
    print('2. Remove an athlete')
    print('3. Update an athlete')
    print('4. Lookup an athlete')
    print('5. Show all athletes.')
    print('6. Quit this program')


def main():
    QUIT_NUM = '6'
    records_file_name = 'pr_list.txt'
    records = read_records_file(records_file_name)

    print_menu()
    menu_option = input('What would you like to do? ')

    while menu_option != QUIT_NUM:
        if menu_option == '1':
            name = input('Insert name: ')
            pr = int(input('Current PR: '))
            insert_athlete(records, name, pr)

        elif menu_option == '2':
            name = input('Remove name: ')
            remove_athlete(records, name)

        elif menu_option == '3':
            name = input('Update name: ')
            pr = int(input('New PR: '))
            update_athlete(records, name, pr)

        elif menu_option == '4':
            name = input('Lookup name: ')
            lookup_athlete(records, name)

        elif menu_option == '5':
            show_all_athletes(records)

        else:
            print('Sorry, that\'t not a valid option.')

        print_menu()
        menu_option = input('What would you like to do? ')

    print('Bye!')

if __name__ == '__main__':
    main()

