'''
Rock_Paper_Scissors_Lizard_Spock.py -- Nguyen Hung Anh -- 09/18/2023
A program that allows the user to play a round of rock, paper, 
scissors, lizard, spock against the computer. 
The rules for the game can be found in the diagram below.
'''
import random

# Function to determine the winning player based on user and computer decisions
def winning_player(user_decision, computer_decision):
    win_player = 0
    
    if user_decision == computer_decision:
        win_player = 1
    elif user_decision == "rock":
        if computer_decision == "scissors" or computer_decision == "lizard":
            win_player = 1
        else:
            win_player = 2
    elif user_decision == "paper":
        if computer_decision == "rock" or computer_decision == "spock":
            win_player = 1
        else:
            win_player = 2
    elif user_decision == "scissors":
        if computer_decision == "paper" or computer_decision == "lizard":
            win_player = 1
        else:
            win_player = 2
    elif user_decision == "lizard":
        if computer_decision == "paper" or computer_decision == "spock":
            win_player = 1
        else:
            win_player = 2
    elif user_decision == "spock":
        if computer_decision == "rock" or computer_decision == "scissors":
            win_player = 1
        else:
            win_player = 2
            
    return win_player

# Main function to play the game
def main():
    # Generate a random number to represent the computer's choice
    i_rand_num = random.randint(1, 5)
    # Map the random number to a corresponding choice for the computer
    if i_rand_num == 1:
        s_computer = "rock"
    elif i_rand_num == 2:
        s_computer = "paper"
    elif i_rand_num == 3:
        s_computer = "scissors"
    elif i_rand_num == 4:
        s_computer = "lizard"
    else:
        s_computer = "spock"
    
    # Take input from the user and convert it to lowercase
    user_choice = (input("Rock, paper, scissors, lizard, or spock? ")).lower()
    
    # Print the computer's choice
    print("Computer chose", s_computer)
    
    # Determine the winner based on user and computer choices
    win_result = winning_player(user_choice, s_computer)

    # Print the result of the game
    if win_result == 1:
        print("You Win!")
    else:
        print("You Lose!")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()

