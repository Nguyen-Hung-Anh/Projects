/*
Asks for an integer between 10 and 25.
Dynamically allocates space for that many integers, exits if allocation fails.
Calls fill_array to assign random values, then prints them.
Increases each value by one with increase_all_by_one.
Finds the highest number with find_extrema, printing the highest and lowest.
Frees memory and sets pointer to NULL.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SEED 21

// Function prototypes
void fill_array(int *arr, int size);
void increase_all_by_one(int *arr, int size);
void find_extrema(int *arr, int size, int *max, int *min);

int main() {
    // Task 1: Ask the user for an int between 10 and 25
    int size;
    int max, min;
    int *arr;
    srand(SEED);    
    
    printf("Enter an integer (between 10 and 25): ");
    scanf("%d", &size);

    // Task 2: Dynamically allocate memory for the array
    arr = (int*)malloc(size*sizeof(int));
    
    if(arr == NULL) {
        printf("Error: Memory allocation failed.\n");
        exit(1);        
    }
    
    // Task 3: Fill the array with random numbers
    fill_array(arr, size);

    // Task 4: Print the randomly generated numbers
    printf("\nRandomly generated numbers:\n");
    for(int i =0; i < size; i++) {
        printf("%d\n", arr[i]);
    }
    printf("\n");

    // Task 5: Increase all numbers in the array by one
    increase_all_by_one(arr, size);

    // Task 6: Print the numbers after increasing all by one
    printf("Numbers after increasing all by one:\n");
    for(int i = 0; i < size; i++) {
        printf("%d\n", arr[i]);
    }
    printf("\n");

    // Task 7: Find the maximum and minimum numbers in the array
    find_extrema(arr, size, &max, &min);

    // Task 8: Print the largest and smallest numbers
    printf("Largest number: %d\n", max);
    printf("Smallest number: %d\n", min);

    // Task 9: Free dynamically allocated memory
    free(arr);
    arr = NULL;

    return 0;
}

// Function to fill the array with random numbers
void fill_array(int *arr, int size) {
    for(int i = 0; i < size; i++) {
        arr[i] = rand() % 100;
    }    
}

// Function to increase all numbers in the array by one
void increase_all_by_one(int *arr, int size) {
    for(int i = 0; i < size; i++) {
        arr[i]++;
    }
}

// Function to find the maximum and minimum numbers in the array
void find_extrema(int *arr, int size, int *max, int *min) {
    *max = arr[0];
    *min = arr[0];

    for(int i = 1; i < size; i++) {
        if(arr[i] > *max) {
            *max = arr[i];
        }

        if(arr[i] < *min){
            *min = arr[i];
        }
    }
}