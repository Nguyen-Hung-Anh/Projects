'''
While_loops_prime_factorization -- Nguyen Hung Anh -- 09/19/2023
This program compute the prime factorization of a user-entered positive integer.
'''

def print_prime_factorization(i_user_number):
    while i_user_number < 0:
    i_divisor_number = 2
    result = i_user_number % i_divisor_number
    
    
    while result != 0:
        i_divisor_number = i_divisor_number + 1
    
        
         
                 
def main():
    get_number = 0
    i_answer = print_prime_factorization(get_number)
    get_number = int(input("Enter a number to factor: "))
                     
if __name__=="__main__":
    main()
    
