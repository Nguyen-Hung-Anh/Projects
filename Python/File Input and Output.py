'''
File_input_and_output.py -- Nguyen Hung Anh -- 10/20/2023
This program reads a file, counts words, and reports the number of words and unique words.
Function: unique_elements(lst): Returns the count of unique elements without modifying the list.
Main: Asks for a file, reads it, and reports word counts.
Example isalpha() Usage: Demonstrates str.isalpha() for checking alphabetic characters.
Note: Save the test file, "poem.txt," in the code directory for testing.
'''

# Function to check if a word contains alphabetic characters
def is_alphabet(word):
    for c in word:
        if c.isalpha():
            return True
    return False

# Function to count total words, unique words, and their frequencies
def count_word(file_name):
    # Open the file in read mode
    poem_fo = open(file_name, 'r')

    # Read the entire content of the file
    text = poem_fo.read()

    # Split the content into words
    words = text.split()

    # Initialize variables for counting
    count = 0
    l_alphabets= []

    # Loop through each word
    for word in words:
        remove_space = word.strip()
        if is_alphabet(remove_space):
            l_alphabets.append(remove_space)

    # Count total words, unique words, and their frequencies
    total_words = len(l_alphabets)
    unique_words = unique_elements(words)
    word_frequency = frequency_count(words)

    # Close the file
    poem_fo.close()

    return total_words, unique_words, word_frequency
    
# Function to count unique elements in a list
def unique_elements(words):
    no_repeat = []

    # Loop through each word
    for word in words:
        remove_space = word.strip().lower()
        only_letter =""
        for c in remove_space:
            if c.isalpha():
                only_letter += c

        # Check if the word is not in the list and not empty
        if only_letter not in no_repeat and only_letter != "":
            no_repeat.append(only_letter)

    # Count unique elements
    count_unique = len(no_repeat)

    return count_unique

# Function to count frequency of words
def frequency_count(word_list):
    word_frequency = {}

    # Loop through each word
    for word in word_list:
        remove_space = word.strip().lower()
        only_letter = ""
        for c in remove_space:
            if c.isalpha():
                only_letter += c

        # Check if the word is not empty
        if only_letter != "":
            # Update word frequency dictionary
            if only_letter in word_frequency:
                word_frequency[only_letter] += 1
            else:
                word_frequency[only_letter] = 1
                
    return word_frequency

# Main function
def main():
    # Ask for the file name
    name_file = input("Count the words in which file? ")

    # Count total words, unique words, and their frequencies
    total_words, total_unique_words, word_frequency = count_word(name_file)

    # Print the results
    print(f"There are {total_words} words in the file.")
    print(f"There are {total_unique_words} unique words in the file.")
    print("Word frequencies:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

# Check if the script is being run directly
if __name__ == "__main__":
    main()