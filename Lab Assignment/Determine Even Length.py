# Practice in the class
def main():
    s_word = input("Word. ")
'''
    i = 0
    while i < len(s_word):
        i = i+1
        if i % 2 == 0:
            print("You have even string")
        else:
            print("You do not have event string")
'''
b_all_even_len = True       
while s_word != "":
    if len(s_word) % 2 != 0:
        b_all_even_len = False

    s_word = input("Word. ")
print("all were even:", b_all_even_len)

if __name__=="__main__":
    main()
