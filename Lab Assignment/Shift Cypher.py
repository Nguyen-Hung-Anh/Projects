'''
Shift_cypher.py -- Nguyen Hung Anh -- 10/11/2023
# This program, shift_cypher_lab.py, decodes a message using a shift cipher.
# Functions: shift_character_right(char, alphabet, shift) and shift_string_right(encrypted_word, alphabet, shift).
# Displays a sample of decoded text for each shift, lets the user select the correct shift, and shows the full decrypted text.
# Uppercase letters are considered before lowercase. Non-alphabetical characters remain unchanged.
# Assumes cyphertext.py is in the same directory.
'''
import cyphertext

print(cyphertext.cyphertext)

def shift_character_right(char, alphabet, shift):
    if char in alphabet:
        location_char = alphabet.index(char)
        new_location_char = (shift + location_char) % len(alphabet)
        char = alphabet[new_location_char]
    return char
def shift_string_right(encrypted_word, alphabet, shift):
    new_word = ""
    for j in range(len(encrypted_word)):
        new_char = encrypted_word[j]
        if encrypted_word[j] in alphabet:
            new_char = shift_character_right(encrypted_word[j], alphabet, shift)
        new_word += new_char
    return new_word
    
def main():
    alphabet = "ABCDEFGHIJLKMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz"
    ten_char = cyphertext.cyphertext [0:10]
    for i in range(52):
        new_word = shift_string_right(ten_char, alphabet, i)
        print(f'Shift {i} : {new_word}')
    correct_shift = int(input("Enter the correct shift: "))
    decrypt_text = shift_string_right(cyphertext, alphabet, correct_shift)
    print(decrypt_text)
    
if __name__ == "__main__":
    main()
