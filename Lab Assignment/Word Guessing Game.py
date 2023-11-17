'''
Word_guessing_game.py --Nguyen Hung Anh-- 2023-09-28
This program will allow players to set words and automatically
reveal the correct positions of letters that have been correctly guessed,
as they are guessed at each round.
'''
def gettingword():
    s_input = input("Word: ").lower()
    return s_input

def create_the_answer(answer):
    return ['_'] * len(answer)

def ask_letters():
    s_letter = input(" Letter to try: ").lower()
    return s_letter

def checking(user_letter, original_word, underscores):
    index = 0
    while index < len(original_word):
        if original_word[index] == user_letter:
            underscores[index] = user_letter
        index += 1
    return underscores

def print_underscores(underscores):
    i = 0
    while i < len(underscores):
        print(underscores[i], end="")
        i += 1   

def main():
    original_word = gettingword()
    underscores  = create_the_answer(original_word)
    rounds = 0
    print_underscores(underscores)
    while '_' in underscores:
        user_letter = ask_letters()
        rounds += 1
        underscores = checking(user_letter, original_word, underscores)
        print_underscores(underscores)    
    print()
    print(f"Well done, it took you {rounds} rounds.")

if __name__ =="__main__":
    main()
