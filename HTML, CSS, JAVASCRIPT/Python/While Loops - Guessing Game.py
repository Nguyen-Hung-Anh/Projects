''' 
While_loop_guessing_game -- Nguyen Hung Anh -- 09/22/2023
 This program generates a random number (1-100), asks the user to guess.
 Provides feedback on whether the guess is too high, too low, or correct.
 Exits immediately upon correct guess. Assumes valid integer inputs.
'''
import random
def main():
    i_rand_num = random.randint(1, 100)
    user_number = int(input("Guess a number: "))
    while user_number != i_rand_num:
        if user_number == i_rand_num:
            print("That was it!")
        elif user_number <= i_rand_num:
            print("Too low!")
        else: 
            print("Too high!")
        user_number = int(input("Guess a number: "))     

if __name__ == "__main__":
    main()
