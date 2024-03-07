'''
While_loop_input_validation_loop -- Nguyen Hung Anh -- 09/22/2023
This program  allows a user to enter their selection for a
game of Rock, Paper, Scissors
'''

def get_rps_input():
    selection_RPS = input("Rock, Paper, or Scissors? ").lower()
    while selection_RPS != "rock" and selection_RPS != "paper" and selection_RPS != "scissors":
        if selection_RPS == "Rock":
            return selection_RPS
        elif selection_RPS == "Paper":
            return selection_RPS
        elif selection_RPS == "Scissors":
            return selection_RPS
        else:
            print("Invalid input.")
        selection_RPS = input("Rock, Paper, or Scissors? ").lower()
    return selection_RPS
        
def main():
    f_correct = get_rps_input()
    print("Your entered:", f_correct)

if __name__=="__main__":
    main()
