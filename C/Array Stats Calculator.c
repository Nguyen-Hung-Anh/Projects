/*
The fill_array function takes the array and its size as arguments, populates the array with user input.
The biggest function takes the array and its size, returns the largest number in the array.
The smallest function takes the array and its size, returns the smallest number in the array.
The my_range function takes the largest and smallest numbers found, returns their difference.
Print the result of my_range in the main function with the format "RANGE: result".
*/

// Function to fill the array with user input

#include <stdio.h>

void fill_array(int array[], int len) {
    int user_num;
    for(int i = 0; i < len; i++) {
        printf("Enter an integer: ");
        scanf("%d", &user_num);
        array[i] = user_num;
    }
}

// Function to find the biggest element in the array
int biggest(int array[], int len) {
    int max = array[0];

    for(int i = 1; i < len; i++) {
        if(array[i] > max) {
            max = array[i];
        }
    }
    return max;
}

// Function to find the smallest element in the array
int smallest(int array[], int len) {
    int min = array[0];

    for(int i = 1; i < len; i++) {
        if(array[i] < min) {
            min = array[i];
        }
    }
    return min;
}

// Function to calculate the range of the array
int my_range(int biggest, int smallest) {
    return biggest - smallest;
}

int main() {
	int arr[10];
	fill_array(arr, 10);
	int big_result = biggest(arr, 10);
	int small_result = smallest(arr, 10);
	int range = my_range(big_result, small_result);	
	printf("RANGE: %d\n", range);
	return 0;
}
