'''
Let's_make_a_deal.py -- Nguyen Hung Anh -- 10/04/2023

# Assignment Part 1:
# This program simulates one round of the "Let's Make a Deal" game.
# It prompts the user to select a door (1, 2, or 3) and ensures valid input.
# The host opens another door with a goat behind it, then asks if the user wants to switch doors.
# The program reveals whether the user won a car or a goat based on their final choice.

# Assignment Part 2:
# The program is enhanced to run multiple simulations with randomized door selection and fixed strategies.
# The user chooses a strategy at the start (keep original door or always switch).
# The function run_simulations(N, keep_original_door) runs N simulations and returns the winning probability.
# The main program runs the automated simulations 100 times for both strategies and prints the results.
# It analyzes the probabilities to determine which strategy is more likely to win the car.
'''

import random

def run_simulations(N, keep_original_door):
    # How many repetitions
    N = int(N)
    i = 0
    win = 0
    
    for i in range(N):
        random_choice_door = random.randint(1, 3) # Randomized door selection
        random_prize_door = random.randint(1, 3) # Randomly choose the prize door
        random_open_door = random.randint(1, 3) # Randomly choose to open door

        # Make sure do not open the car door in two cases
        if random_prize_door == random_choice_door:
            while random_open_door == random_prize_door:
                random_open_door = random.randint(1, 3)
        else:
            while random_open_door == random_choice_door or random_open_door == random_prize_door:
                random_open_door = random.randint(1, 3)
                
        # If user change, make sure to automatically change
        if not keep_original_door:
            strategy = random.randint(1, 3)
            while strategy == random_open_door or strategy == random_choice_door:
                strategy = random.randint(1, 3)
            random_choice_door = strategy
        else:
            random_choice_door = random_choice_door

        # Probability of winning
        if random_prize_door == random_choice_door:
            win += 1
        else:
            win = win

    f_probability = float(win/N)

    return f_probability

def main():
    # Ask the user to start
    s_input = input("Do you want to [p]lay the Monty Hall Game, or [r]un some simulations? ").lower()
    while s_input != 'p' and s_input != 'r':
        s_input = input("Do you want to [p]lay the Monty Hall Game, or [r]un some simulations? ").lower()

    # Repetitions that users want to 
    i_repetitions = input("How many repetitions? ")
    i_repetitions = int(i_repetitions)
    
    s_keep = input("Keep original door? [Y/n] ").lower()
    while s_keep != 'y' and s_keep != 'n':
        s_keep = input("Keep original door? [Y/n] ").lower()

    if s_keep == 'n':
        change = True
    else:
        change = False
        
    answer = run_simulations(i_repetitions, not change)
    print(answer)

if __name__ == "__main__":
    main()
