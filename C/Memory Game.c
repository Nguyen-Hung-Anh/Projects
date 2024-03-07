/*
Array Initialization: The program generates a 3x4 dynamically allocated array filled 
with hidden letters (A, B, C, D, E, F) placed randomly in pairs.

User Input: The user inputs the row and column of two locations to reveal the letters 
at those positions in the array.

Array Redraw: After each guess, the array is redrawn to reveal the letters in the 
chosen positions. If the letters match, those spots are replaced with blank spaces; 
otherwise, the array is redrawn with X in place of the letters.

Game Continuation: The user continues guessing until all matches are found or until 
they have 5 failed attempts.

Win/Loss Notification: Upon completion of the game (either by finding all matches or reaching 
5 failed attempts), the program informs the user whether they won or lost, and then exits.

Modular Structure: The program employs functions to handle various tasks, promoting 
code organization and readability.
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> // Include stdbool.h for boolean data type

#define N 3
#define M 4

#define SEED 21

char** create_table();
void print_table_x(char** two_d_array);
void reveal_letter(char** two_d_array, int row1, int column1, int row2, int column2);
void check_pair(char** two_d_array, int row1, int column1, int row2, int column2);

int main() {
	int row1, column1, row2, column2;

  char** answer_table = create_table();
  // Game loop
  int attempts = 0;
  while (attempts < 5) { // Use attempts as a loop condition
	  print_table_x(answer_table);
  	printf("Enter coordinates of two locations (e.g., 0 0 1 1): ");
    scanf("%d %d %d %d", &row1, &column1, &row2, &column2);

    // Check if coordinates are valid
    if (row1 < 0 || row1 >= N || column1 < 0 || column1 >= M ||
       	row2 < 0 || row2 >= N || column2 < 0 || column2 >= M) {
        printf("Invalid coordinates. Try again.\n");
        continue;
    }
    reveal_letter(answer_table, row1, column1, row2, column2);
		check_pair(answer_table, row1, column1, row2, column2);

    attempts++;
  }
  printf("Sorry, you've reached the maximum number of attempts. You lost.\n");
    
  // Free dynamically allocated memory
  for (int i = 0; i < N; i++) {
  	free(answer_table[i]);
  }
  free(answer_table);

  return 0;
}

char** create_table() {
	char **two_d_array;
  srand(SEED);
  two_d_array = malloc(sizeof(char *) * N); // Allocate memory for characters
  if (two_d_array == NULL) {
  	printf("Memory allocation failed\n");
    exit(1);
 	}
  for(int i = 0; i < N; i++) {
  	two_d_array[i] = malloc(sizeof(char) * M); // Allocate memory for characters
    if (two_d_array[i] == NULL) {
    	printf("Memory allocation failed\n");
      exit(1);
    }
  }

  // Define an array to hold the count of each letter
  int counts[6] = {0}; // Initialize to 0
  char letters[6] = {'A', 'B', 'C', 'D', 'E', 'F'};

  // Assign letters randomly to the array
  for(int i = 0; i < N; i++) {
  	for(int j = 0; j < M; j++) {
    	int index;
      	do {
   		     index = rand() % 6;
   	    } while (counts[index] >= 2); // Check if letter count exceeds 2
        two_d_array[i][j] = letters[index];
        counts[index]++;
   }
 }

  return two_d_array;
}

void print_table_x(char** two_d_array) {
	for(int i = 0; i < N; i++) {
  	for(int j = 0; j < M; j++) {
		  if (two_d_array[i][j] == ' ') {
			printf(" ");
			} else {
    	printf("X");
			}
    }
      printf("\n");
 }
}

void reveal_letter(char** two_d_array, int row1, int column1, int row2, int column2) {
	for(int i = 0; i < N; i++) {
		for(int j = 0; j < M; j++) {
    	if((i == row1 && j == column1) || (i == row2 && j == column2)) {
      	printf("%c", two_d_array[i][j]);
      }
      else {
        printf("X");
     	}
     }
     printf("\n");
  }
}

void check_pair(char** two_d_array, int row1, int column1, int row2, int column2) {
	if (two_d_array[row1][column1] == two_d_array[row2][column2] && two_d_array[row1][column1] != ' ') {
  	printf("Match found!\n");
    two_d_array[row1][column1] = ' ';
    two_d_array[row2][column2] = ' ';
  } else {
    printf("Sorry, no match!\n");
  }

}

