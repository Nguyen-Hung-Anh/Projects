'''
File_input_and_output.py -- Nguyen Hung Anh -- 10/20/2023
This program reads a file, counts words, and reports the number of words and unique words.

Function: unique_elements(lst): Returns the count of unique elements without modifying the list.

Main: Asks for a file, reads it, and reports word counts.

Example isalpha() Usage: Demonstrates str.isalpha() for checking alphabetic characters.

Note: Save the test file, "poem.txt," in the code directory for testing.
'''

def is_alphabet(word):
    for c in word:
        if c.isalpha():
            return True
    return False

def count_word(file_name):
    poem_fo = open(file_name, 'r')

    text = poem_fo.read()

    words = text.split()

    count = 0

    l_alphabets= []

    for word in words:
        remove_space = word.strip()
        if is_alphabet(remove_space):
            l_alphabets.append(remove_space)

    total_words = len(l_alphabets)
    unique_words = unique_elements(words)
    word_frequency = frequency_count(words)

    return total_words, unique_words, word_frequency
    
def unique_elements(words):

    no_repeat = []

    for word in words:
        remove_space = word.strip().lower()
        only_letter =""
        for c in remove_space:
            if c.isalpha():
                only_letter += c

        if only_letter not in no_repeat and only_letter != "":
            no_repeat.append(only_letter)

    count_unique = len(no_repeat)

    return count_unique

def frequency_count(word_list):
    word_frequency = {}

    for word in word_list:
        remove_space = word.strip().lower()
        only_letter = ""
        for c in remove_space:
            if c.isalpha():
                only_letter += c

        if only_letter != "":
            if only_letter in word_frequency:
                word_frequency[only_letter] += 1
            else:
                word_frequency[only_letter] = 1
                
    return word_frequency

    
def main():
    name_file = input("Count the words in which file? ")
    total_words, total_unique_words, word_frequency = count_word(name_file)

    print(f"There are {total_words} words in the file.")
    print(f"There are {total_unique_words} unique words in the file.")
    print("Word frequencies:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
