'''
Word_guessing_game.py --Nguyen Hung Anh-- 2023-09-28
This program will allow players to set words and automatically
reveal the correct positions of letters that have been correctly guessed,
as they are guessed at each round.
'''
# Function to get the word from the user
def gettingword():
    s_input = input("Word: ").lower()
    return s_input

# Function to create the answer by converting each letter to underscores
def create_the_answer(answer):
    return ['_'] * len(answer)

# Function to ask the user for a letter to try
def ask_letters():
    s_letter = input("Letter to try: ").lower()
    return s_letter

# Function to check if the guessed letter is correct and update underscores
def checking(user_letter, original_word, underscores):
    index = 0
    while index < len(original_word):
        if original_word[index] == user_letter:
            underscores[index] = user_letter
        index += 1
    return underscores

# Function to print underscores representing the guessed letters
def print_underscores(underscores):
    for char in underscores:
        print(char, end="")
    print()

# Main function to run the word guessing game
def main():
    original_word = gettingword()
    underscores = create_the_answer(original_word)
    rounds = 0
    print_underscores(underscores)
    
    # Continue the game until all letters are guessed
    while '_' in underscores:
        user_letter = ask_letters()
        rounds += 1
        underscores = checking(user_letter, original_word, underscores)
        print_underscores(underscores)
    
    # Print the number of rounds taken to guess the word
    print(f"Well done, it took you {rounds} rounds.")

if __name__ == "__main__":
    main()
