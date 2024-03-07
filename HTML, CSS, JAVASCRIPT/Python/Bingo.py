# Practices in the class

# forward iteration and index math
def reverse(s_word):
    s_reversed = ""
    for i in range(len(s_word)):
        s_reversed += s_word[len(s_word)-i-1]
    return s_reversed

# version 2: barkward iteration

def reverse(s_word):
    s_reversed = ""
    for i in range(len(s_word)-1, -1, -1):
        s_reversed += s_word[i]
    return s_reversed
# version 3:
def reverse(s_word):
    s_reversed = ""
    for i in range(len(s_word)):
        s_reversed = s_word[i] + s_reversed

def main():
    s_my_word = input("Word: ")
    #s_char = input("Char: ")
    print(reverse(s_my_word))

if __name__ == "__main__":
    main()
    
