'''
Project_1_Math_Tutor.py -- Nguyen Hung Anh -- 09/28/2023
This program will randomly select one of addition, subtraction, or multiplication,
and then generate random integers for the user to add, subtract or multiply.
'''

import random

'''
Function to generate an arithmetic problem and return the operator, operands,
and the correct result.
'''
def generate_problem():
    # Generate a random number for operation_num, i_num1, and i_num2
    operation_num = random.randint(1, 3)
    i_num1 = random.randint(1, 12)
    i_num2 = random.randint(1, 12)

    # Determine the operation based on operation_num
    if operation_num == 1:
        operation = 'addition'
        result = i_num1 + i_num2
    elif operation_num == 2:
        operation = 'subtract'
        if i_num1 > i_num2:
            result = i_num1 - i_num2
        else:
            # Swap num1 and num2 to ensure a positive result
            tempnum = i_num1
            i_num1 = i_num2
            i_num2 = tempnum
            result = i_num1 - i_num2
    else:
        operation = 'multiplication'
        result = i_num1 * i_num2
        
    return operation, i_num1, i_num2, result

     
# The main function for the Arithmetic Tutor program
def main():
    print("Welcome to the Arithmetic Tutor")
    user_input = input("Practice arithmetic? (Y/n) ").lower()
    while user_input != 'y' and user_input != 'n':
        user_input = input("Practice arithmetic? (Y/n) ").lower()
        
    # Start practicing arithmetic problems
    while user_input == 'y':
        attempts = 0
        operator, i_num1, i_num2, result = generate_problem()
        
        # An infinite loop that will end when one of the two conditions is met
        while True:
            if operator == 'addition':
                user_answer = input(f"{i_num1} + {i_num2} = ")
            elif operator == 'subtract':
                user_answer = input(f"{i_num1} - {i_num2} = ")
            else:
                user_answer = input(f"{i_num1} * {i_num2} = ")
            
            # Check if the user's answer is correct
            if user_answer == str(result):
                print("Correct!")
                break
            # The user fails more than 3 times
            elif attempts == 2:
                print(f"Sorry, that's incorrect. The correct answer is {result}.")
                break
            else:
                print("Sorry, that's incorrect.")
                attempts += 1
                
        user_input = input("Continue Practicing? (Y/n) ").lower()
        while user_input != 'y' and user_input != 'n':
            user_input = input("Practice arithmetic? (Y/n) ").lower()
        
    if user_input == 'n':
        print("Bye!")

if __name__ == "__main__":
    main()
