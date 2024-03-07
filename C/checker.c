#include<stdio.h>

// Function to count occurrences of a number in a 2D array and print their positions
int how_many_slots(int **two_d_array, int row, int column, int number) {
    int count = 0; // Initialize count to 0

    // Loop through each row
    for(int i = 0; i < row; i++) {
        // Loop through each column in the current row
        for(int j = 0; j < column; j++) {
            // If the current element matches the number
            if(number == two_d_array[i][j]) {
                // Print the position of the element
                printf("Row: %d, Column: %d\n", i, j);
                count++; // Increment count
            }
        }
    }
    return count; // Return the total count of occurrences
}
