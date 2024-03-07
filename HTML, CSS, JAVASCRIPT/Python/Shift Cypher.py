'''
Shift_cypher.py -- Nguyen Hung Anh -- 10/11/2023
# This program, shift_cypher_lab.py, decodes a message using a shift cipher.
# Functions: shift_character_right(char, alphabet, shift) and shift_string_right(encrypted_word, alphabet, shift).
# Displays a sample of decoded text for each shift, lets the user select the correct shift, and shows the full decrypted text.
# Uppercase letters are considered before lowercase. Non-alphabetical characters remain unchanged.
# Assumes cyphertext.py is in the same directory.
'''
import cyphertext

# Print the encrypted text from the imported module
print(cyphertext.cyphertext)

# Function to shift a character to the right within an alphabet
def shift_character_right(char, alphabet, shift):
    if char in alphabet:
        # Find the index of the character in the alphabet
        location_char = alphabet.index(char)
        # Calculate the new index after shifting
        new_location_char = (shift + location_char) % len(alphabet)
        # Get the character at the new index
        char = alphabet[new_location_char]
    return char

# Function to shift a string to the right within an alphabet
def shift_string_right(encrypted_word, alphabet, shift):
    new_word = ""
    # Iterate through each character in the string
    for j in range(len(encrypted_word)):
        new_char = encrypted_word[j]
        # Check if the character is in the alphabet
        if encrypted_word[j] in alphabet:
            # Shift the character and update the new word
            new_char = shift_character_right(encrypted_word[j], alphabet, shift)
        new_word += new_char
    return new_word

# Main function to decrypt the text
def main():
    # Define the alphabet
    alphabet = "ABCDEFGHIJLKMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz"
    # Take the first ten characters of the encrypted text
    ten_char = cyphertext.cyphertext[0:10]
    # Iterate through possible shifts
    for i in range(52):
        # Decrypt the text with the current shift and print the result
        new_word = shift_string_right(ten_char, alphabet, i)
        print(f'Shift {i} : {new_word}')
    # Ask the user to input the correct shift
    correct_shift = int(input("Enter the correct shift: "))
    # Decrypt the entire text with the correct shift
    decrypt_text = shift_string_right(cyphertext.cyphertext, alphabet, correct_shift)
    # Print the decrypted text
    print(decrypt_text)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()