/*
Create a program named palindrome.c
Declare an array capable of holding 80 characters (including null terminator)
Use scanf to fill the array with letters (assuming no spaces are entered)
Write a function is_palindrome to check if the characters form a palindrome
The function should take the array of characters and its length as arguments and return 1 if palindrome, 0 otherwise
In the main function, call is_palindrome and print "PAL" or "NOT PAL" accordingly
Add a comment to the program answering how it would differ if the array held an odd number of characters instead of an even number
*/

#include <stdio.h>
#include <string.h>


int is_palindrome(char str[], int length) {
	int start = 0;
  int end = length - 2;  // Ignore null terminator

  while (start < end) {
  	if (str[start] != str[end]) {
    	return 0; // Not a palindrome
    }
    start++;
    end--;
 	}

  return 1; // Palindrome
}

int main() {
	char array[80];
  printf("Enter a string of up to 79 characters: ");
  scanf("%79s", array);

  // Calculate the length of the input string
  int length = strlen(array) + 1; // Including null terminator
	array[length - 1] = '\0';    
  if (is_palindrome(array, length)) {
  	printf("PAL\n");
  } else {
    	printf("NOT PAL\n");
  }

 	return 0;
}

/*
If the array held an odd number of characters instead of an even number of 
characters, the implementation of the 'is_palindrome' function wouldn't need 
any modification. The function compares characters from the start and end 
of the array, and the middle character (if there is one) is ignored because 
it will always be the same for both odd and even-length palindromes. 
Thus, the program would work correctly for both odd and even-length 
palindromes without any changes.	
*/
