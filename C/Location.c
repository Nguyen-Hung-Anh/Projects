/*
Create a program named location.c with an array of 8 characters. 
Fill the array using scanf, prompting the user for letters without spaces. 
Then, prompt the user for a letter. Implement a function named location 
that returns -1 if the letter isn't in the array, or the index of 
its first occurrence if it is. Finally, print the function's return value 
in the main function.
*/
#include<stdio.h>

// Function to find the location of a letter in an array
int location(char array[], int length, char letter) {
    for (int i = 0; i < length; i++) {
        if (array[i] == letter) {
            return i;  // Found the letter, return its index
        }
    }
    return -1;  // Letter not found, return -1
}

int main() {
    char letter[8];
    char searchLetter;
    int index;

    // Prompt the user to enter 7 letters
    printf("Enter 7 letters: ");
    scanf("%7s", letter); // Read up to 7 letters to prevent buffer overflow
    
    // Prompt the user to enter a letter to search for
    printf("Enter a letter to search: ");
    scanf(" %c", &searchLetter);
    letter[7] = '\0'; // Null terminate the array to ensure proper string handling
    
    // Call the location function to find the index of the search letter
    index = location(letter, 8, searchLetter);
    
    // Print the index of the search letter found in the array
    printf("%d\n", index);
    
    return 0;
}
