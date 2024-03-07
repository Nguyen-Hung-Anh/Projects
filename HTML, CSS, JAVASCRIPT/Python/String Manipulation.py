'''
String_Manipulation.py -- Nguyen Hung Anh -- 10/05/2023

This program writes four functions

1. replace(): This function should return a new version of replace_within
where all instances of old have been replaced with new

2. without_spaces(): This function should return a new version of the string
which has no spaces

3. is_palindrome(): This function should return True if the input string is a palindrome

4. locate_within_string(): This function should find string needle on string haystack
'''
def replace(replace_within, old, new):
    s_changed = "" # accumulator for string
    for i in range(len(replace_within)):
        if replace_within[i] == old:
            # if original == old => change old to new
            s_changed += new
        else:
            # if original != old => keep original
            s_changed += replace_within[i]
    return s_changed
                   
def without_spaces(original_word):
    s_output = "" # accumulator for string
    for i in range(len(original_word)):
        if original_word[i] != " ":
            # if original != space => add original
            s_output += original_word[i]
    return s_output

def is_palindrome(original_word):
    original_word = without_spaces(original_word)
    reversed_word = ""
    # start from last character
    # ends before the first char 
    # backward
    for i in range(len(original_word)-1, -1, -1): 
        reversed_word += original_word[i]
    
        
    return original_word == reversed_word

def locate_within_string(haystack, needle):
    found = False
    for i in range(len(haystack) - len(needle) +1):
        if haystack[i : i+ len(needle)] == needle:
            print(f"The substring '{needle}' appears at index {i} within '{haystack}'")
            return i
    if not found:
        print("String was not found")
    return len(haystack)
        
def main():
    # TRY TO PRINT IN ORDER ON MOODLE
    s_input = input("Enter a string: ").lower()
    
    answer2 = is_palindrome(answer)
    if answer2:
        print(f"{s_input} is a palindrome")
    else:
        print(f"{s_input} is not a palindrome")
    print()
        
    user_input_old = input("What's your old letter? ")
    user_input_new = input("What's your new letter? ")
    answer3 = replace(s_input, user_input_old, user_input_new)
    
    print(f"Replacing '{user_input_old}' with '{user_input_new}' in '{s_input}' yeilds '{answer3}'")
    print()
    
    print(f"Removing spaces from '{s_input}' yeilds '{answer}'")
    print()
    
    s_user_needle = input("Your needle: ")
    answer4 = locate_within_string(s_input, s_user_needle)
    print(answer4)

if __name__ == "__main__":
    main()
