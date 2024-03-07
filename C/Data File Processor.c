/*
Program reads an integer from the command line argument to determine the number of items to read from "data.txt".
Counts occurrences of single integers ranging from 0 to 9 in the file.
Prints the number that occurred first.
Prints counts of each integer from 0 to 9.
Prompts the user to enter their two favorite integers between 0 and 9.
Prints out the count of occurrences for each favorite integer entered by the user.
*/

#include<stdio.h>
#include<stdlib.h>

// Function prototypes
int read_data(int array[], int times);
void print_data(int array[], int times);
void print_favorites(int array[], int fav1, int fav2);

int main(int argc, char *argv[]) {
    // Read the number of times from command line argument
    int times = atoi(argv[1]);
    int array[10];
    
    // Initialize array elements to 0
    for(int i = 0; i < times; i++) {
        array[i] = 0;
    }

    // Read data from file and populate the array
    read_data(array, times);
    
    // Print the data in the array
    print_data(array, times);

    // Prompt user to enter their favorite numbers
    int fav1;
    int fav2;
    printf("What's your first fav num?: ");
    scanf("%d", &fav1);
    printf("What's your second fav num?: ");
    scanf("%d", &fav2);
    
    // Print occurrences of favorite numbers
    print_favorites(array, fav1, fav2);

    return 0;
}

// Function to read data from file and populate the array
int read_data(int array[], int times) {
    FILE *file = fopen("data.txt", "r");
    if(file == NULL) {
        printf("Error opening file.\n");
        exit(1);
    }

    int first_number;
    fscanf(file, "%d", &first_number); // Read and ignore the first number
    
    // Read the numbers from the file and update array accordingly
    int num;
    rewind(file); // Set file pointer to beginning of file
    fseek(file, 0, SEEK_SET);
    for(int i = 0; i < times; i++) {
        fscanf(file, "%d", &num);
        array[num]++;
    }
    
    fclose(file);
    return first_number; // Return the first number from the file (unused in this implementation)
}

// Function to print the data in the array
void print_data(int array[], int times) {
    printf("Number Occurrences:\n");
    for(int i = 0; i < 10; i++) {
        printf("%d %d\n", i, array[i]);
    }
}

// Function to print occurrences of favorite numbers
void print_favorites(int array[], int fav1, int fav2) {
    printf("Your favorite numbers and their occurrences:\n");
    printf("%d \t %d\n", fav1, array[fav1]);
    printf("%d \t %d\n", fav2, array[fav2]);
}