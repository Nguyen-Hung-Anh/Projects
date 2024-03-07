/*
Program dynamically allocates memory for a 2D array of integers based on user input for rows and columns.
Populates the array with the sum of row and column indices and prints it using print_array().
Prompts the user for an integer and passes it, along with the array dimensions, to how_many_slots() in checker.c.
how_many_slots() calculates and prints the number of slots containing the entered integer along with their row and column indices.
Frees all allocated memory and sets pointers to NULL.
*/

#include<stdio.h>
#include<stdlib.h>
#include "checker.h" // Include header file for function declaration

// Function prototypes
void fill_array(int **two_d_array, int row, int column);
void print_array(int **two_d_array, int row, int column);

int main() {
    // Variable declarations
    int row, column, number;
    int **two_d_array;

    // Prompt the user to enter the number of rows and columns
    printf("Enter number of rows: ");
    scanf("%d", &row);
    printf("Enter number of columns: ");
    scanf("%d", &column);
    
    // Dynamically allocate memory for 2D array
    two_d_array = malloc(sizeof(int *) * row);
    if(two_d_array == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }
    for(int i = 0; i < row; i++) {
        two_d_array[i] = malloc(sizeof(int) * column);
        if(two_d_array[i] == NULL) {
            printf("Memory allocation failed.\n");
            return 1;
        }
    }

    // Fill the 2D array with values
    fill_array(two_d_array, row, column);

    // Print the 2D array
    printf("2D Array:\n");
    print_array(two_d_array, row, column);

    // Prompt the user to enter a number to search for in the array
    printf("Enter a number: ");
    scanf("%d", &number);
    // Call function to find how many slots contain the entered number
    int slots = how_many_slots(two_d_array, row, column, number);
    printf("Total number of slots containing %d: %d\n", number, slots);
    
    // Free dynamically allocated memory
    for(int i = 0; i < row; i++) {
        free(two_d_array[i]);
    }
    free(two_d_array);
    two_d_array = NULL;

    return 0;
}

// Function to fill the 2D array with values
void fill_array(int **two_d_array, int row, int column) {
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < column; j++) {
            two_d_array[i][j] = i + j;
        }
    }
}

// Function to print the 2D array
void print_array(int **two_d_array, int row, int column) {
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < column; j++) {
            printf("%d ", two_d_array[i][j]);
        }
        printf("\n");
    }
}
