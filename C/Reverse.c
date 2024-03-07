/*
Create a program named reverse.c
Declare an array capable of holding 80 characters (including null terminator)
Use scanf to fill the array with letters (assuming no spaces are entered)
Write a function to reverse the characters in the array without using an additional array
The function should take the array of characters and its length as input
Print the array before and after calling the function
Add a comment in the code answering how the program would differ if the array held an odd number of characters instead of an even number
*/

#include <stdio.h>
#include <string.h>

void reverse(char str[], int length) {
	int start = 0;
	int end = length - 2;  // Ignore null terminator
  while (start < end) {
    char temp = str[start];
   	str[start] = str[end];
    str[end] = temp;
    start++;
		end--;
	}
}

int main() {
	char array[80];
  printf("Enter a string of up to 79 characters: ");
  scanf("%79s", array);

  printf("Original string: %s\n", array);
    
  // Calculate the length of the input string
  int length = strlen(array) + 1; // Including null terminator
	array[length - 1] = '\0';

  reverse(array, length);

  printf("Reversed string: %s\n", array);

  return 0;
}

/*
If the array held an odd number of characters, the middle character would
remain in its place as it wouldn't have a counterpart to swap with.
And the reversal would only occur for pairs of characters around the middle.
So, in the reversal process, the middle character remains unchanged.
*/
