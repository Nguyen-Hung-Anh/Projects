/*
Create a program named prog2.c
Define a struct named data with fields: band_name, song_title, and year
Declare an array of 3 structs in the main function
Call fill_in_structs() to populate the array with user input
Implement find_band() to check if a specified band exists in the array and retrieve the earliest song year
Print the earliest song year and whether the specified band was found
Call dump_data() to print the array of structs in a specified format
Handle input containing spaces carefully
Avoid using global variables
*/

#include <stdio.h>
#include <string.h>

// Struct definition
struct data {
    char band_name[64];
    char song_title[32];
    int year;
};

// Function prototypes
void fill_in_structs(struct data *arr);
int find_band(struct data arr[], char *band_name, int *earliest_year);
void dump_data(struct data *arr);

int main() {
    struct data songs[3];
    int earliest_year;
    
    fill_in_structs(songs);
    
    char band_to_find[64];
    printf("Enter a band name to find: ");
    fgets(band_to_find, sizeof(band_to_find), stdin);
    band_to_find[strcspn(band_to_find, "\n")] = '\0'; // Remove trailing newline
    
    int found = find_band(songs, band_to_find, &earliest_year);
    
    if (found == 1) {
        printf("The band was found in the array of structs.\n");
        printf("The earliest song year is: %d\n", earliest_year);
    } else {
        printf("The band was not found in the array of structs.\n");
    }
    
    printf("\nDumping data:\n");
    dump_data(songs);
    
    return 0;
}

// Function definitions
void fill_in_structs(struct data *arr) {
    for (int i = 0; i < 3; i++) {
        printf("Enter band name for song %d: ", i + 1);
        fgets(arr[i].band_name, sizeof(arr[i].band_name), stdin);
        arr[i].band_name[strcspn(arr[i].band_name, "\n")] = '\0'; // Remove trailing newline
        
        printf("Enter song title for song %d: ", i + 1);
        fgets(arr[i].song_title, sizeof(arr[i].song_title), stdin);
        arr[i].song_title[strcspn(arr[i].song_title, "\n")] = '\0'; // Remove trailing newline
        
        printf("Enter year for song %d: ", i + 1);
        scanf("%d", &arr[i].year);
        getchar(); // Consume newline left in input buffer
    }
}

int find_band(struct data arr[], char *band_name, int *earliest_year) {
		*earliest_year = arr[0].year;
    for (int i = 0; i < 3; i++) {
        if (strcmp(band_name, arr[i].band_name) == 0) {
            if (*earliest_year > arr[i].year) {
                *earliest_year = arr[i].year;
            }
            return 1; // Band found
        }
    }
    return -1; // Band not found
}

void dump_data(struct data *arr) {
    for (int i = 0; i < 3; i++) {
        printf("%s\n%s\n%d\n=====\n", arr[i].band_name, arr[i].song_title, arr[i].year);
    }
}
