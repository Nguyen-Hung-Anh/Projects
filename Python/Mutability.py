'''
Assignment:
    1. Debug each function
    2. Write a 3-4 sentence for each function explaining what is wrong, 
       and how it can be fixed.
    3. Fix each function so that it behaves as indicated in the docstrings.

'''

def initialize_identity_matrix(n: int) -> list:
    '''
    Returns a square matrix (2D list) with 1's on the diagonal, and 0's everywhere else.
    E.g., for n = 2; [[1, 0],
                      [0, 1]]
    Parameter:
        n: [int] the number of rows and columns the matrix should have

    Return:
        l_ident: [list] the n by n identity matrix
    '''
# The issue here is that the list is not being created as intended.
# The line l_ident = [ [0] * n] * n creates a list of lists,
# but all inner lists are references to the same list.
# This leads to unintended changes in multiple rows.
# Instead of using the * operator, use a list comprehension to create distinct inner lists
    l_ident = [[0] * n for _ in range(n)]

    for i in range(n):
        l_ident[i][i] = 1

    return l_ident



def sort_list(l_unsort: list) -> None:
    '''
    Returns a list containing all the elements of l_unsort, but in non-decreasing order.
    Parameter:
        l_unsort: [list] a list of comparable objects (i.e. those that have < defined)

    Return:
        l_sort: [list] a list containing all the elements of l_unsort, 
            in non-decreasing order
    '''
    '''
    We start iterating from the second element (i = 1) because the first element is already considered sorted.
    We store the current element (current_value) that needs to be inserted into the sorted portion of the list.
    We shift elements greater than the current_value to the right until we find the correct position for insertion.
    We insert the current_value into the correct position in the sorted portion of the list.
    '''
    # Iterate over the list starting from the second element
    for i in range(1, len(l_unsort)):
        # Store the current element to be inserted
        current_value = l_unsort[i]
        position = i

        # Shift elements greater than the current value to the right
        while position > 0 and l_unsort[position - 1] > current_value:
            l_unsort[position] = l_unsort[position - 1]
            position -= 1

        # Insert the current value in the correct position
        l_unsort[position] = current_value
    return None
    


def main():

    print(initialize_identity_matrix(3))


    l = [12, 3, 5, 24, 1]
    print("Before:", l)
    sort_list(l)
    print("After:", l)


if __name__ == '__main__':
    main()
