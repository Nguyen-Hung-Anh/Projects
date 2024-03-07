/*
Create a program that displays a menu with four options:
1. Convert cm to inches
2. Convert Celsius to Fahrenheit
3. Convert dollars to Euros
4. Exit
Prompt the user to select an option by entering the corresponding integer.
Upon selection, prompt the user for the value to convert.
Display the result of the conversion.
Display the menu again.
Continue repeating this process until the user selects menu item 4 (Exit).
If the user enters an invalid choice (other than 1, 2, 3, or 4), prompt them to enter a valid choice repeatedly until they do.
*/

#include<stdio.h>
#include<stdlib.h>

// Function to convert centimeters to inches
float cm_to_inches() {
    float user_input;
    printf("Enter your cm: ");
    scanf("%f", &user_input);
    float answer = user_input * 0.393701;
    return answer;
}

// Function to convert Celsius to Fahrenheit
float cel_to_fah() {
    float user_input;
    printf("Enter your temperature in Celsius: ");
    scanf("%f", &user_input);
    float answer = (user_input * 9) / 5 + 32;
    return answer;
}

// Function to convert dollars to Euros
float dollars_to_euros() {
    float user_input;
    printf("Enter dollars: ");
    scanf("%f", &user_input);
    float answer = user_input * 0.93;
    return answer;
}

int main() {
    int user_choice;

    while(1) {
        // Display menu options
        printf("1. Convert cm to inches\n");
        printf("2. Convert Celsius to Fahrenheit\n");
        printf("3. Convert dollars to Euros\n");
        printf("4. Exit\n\n");   
        printf("Choose your option: ");

        scanf("%d", &user_choice);
        
        // Perform conversion based on user's choice
        if(user_choice == 1) {
            float answer1 = cm_to_inches();
            printf("Answer1: %.2f inches\n", answer1);
        } else if(user_choice == 2) {
            float answer2 = cel_to_fah();
            printf("Answer2: %.2f Fahrenheit\n", answer2);
        } else if(user_choice == 3){
            float answer3 = dollars_to_euros(); 
            printf("Answer3: %.2f Euros\n", answer3);
        } else if(user_choice == 4) {
            exit(1); // Exit the program
        } else {
            printf("Invalid Input. Choose again: ");
        }
    }   
    return 0;
}