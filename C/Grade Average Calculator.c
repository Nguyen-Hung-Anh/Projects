/*
Prompt for the number of students.
For each student, input 3 grades.
Calculate the average using calc_avg function.
Print the average for each student.
*/
#include <stdio.h>

// Function prototype for calculating average
float calc_avg(int grade1, int grade2, int grade3);

int main() {
    int number_students;
    int grade1, grade2, grade3;
    
    // Prompt the user for the number of students
    printf("How many students are there in the class:? ");
    scanf("%d", &number_students);
    printf("\n");

    // Loop for each student
    for(int i = 0; i < number_students; i++) {
        printf("Enter grades for student %d:\n", i+1);
        // Prompt for three grades
        printf("Enter grade 1: ");
        scanf("%d", &grade1);
        printf("Enter grade 2: ");
        scanf("%d", &grade2);
        printf("Enter grade 3: ");
        scanf("%d", &grade3);

        // Calculate and print the average for the current student
        float average = calc_avg(grade1, grade2, grade3);
        printf("Average for student %d: %.2f\n\n", i+1, average);
    }

    return 0;
}

// Function to calculate the average of three grades
float calc_avg(int grade1, int grade2, int grade3) {
    float average = (grade1 + grade2 + grade3) / 3.0;
    return average;
}
