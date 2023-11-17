'''
Rock_Paper_Scissors_Lizard_Spock.py -- Nguyen Hung Anh -- 09/18/2023
A program that allows the user to play a round of rock, paper, 
scissors, lizard, spock against the computer. 
The rules for the game can be found in the diagram below.
'''
import random

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
def main():

    i_rand_num = random.randint(1,5)
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
    
    user_choice = (input("Rock, paper, scissors, lizard, or spock? ")).lower()
    
    print("Computer chose", s_computer)
    
    winning_player(user_choice, s_computer)

    if winning_player(user_choice, s_computer) == 1:
        print("You Win!")
    else:
        print("You Lose!")
    
if __name__ == "__main__":
    main()

