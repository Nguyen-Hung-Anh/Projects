/*
Write a program with a get_user_data function:
It takes pointers to two integers and one float.
Asks the user for age, favorite number, and purchase cost.
Doesn't return anything, just prints user's inputs in main().
*/
#include <stdio.h>

// Function to get user data
void get_user_data(int *age, int *number, float *cost) {
    // Prompt the user for age
    printf("Enter your age: ");
    scanf("%d", age);

    // Prompt the user for favorite number
    printf("Enter your favorite number: ");
    scanf("%d", number);

    // Prompt the user for the cost of the last item purchased
    printf("Enter the cost of the last item you purchased: ");
    scanf("%f", cost);
}

int main() {
    // Variable declarations
    int age, number;
    float cost;

    // Call get_user_data function to get user inputs
    get_user_data(&age, &number, &cost);

    // Print user inputs in main function
    printf("\nInformation:\n");
    printf("Age: %d\n", age);
    printf("Favorite Number: %d\n", number);
    printf("Cost of Last Item Purchased: %.2f\n", cost);

    return 0;
}
