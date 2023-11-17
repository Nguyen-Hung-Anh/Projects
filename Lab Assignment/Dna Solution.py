'''
Project_2_dna-identification.py -- Nguyen Hung Anh -- 11/03/2023
This program identifies to whom a sequence of DNA belongs.
'''

# Function to count the occurrences of a subsequence within a DNA sequence.
def count_sequence(dnasequence, subsequence):
    maximum = 0
    for i in range(0, len(dnasequence) - len(subsequence) + 1):    
        current_word = dnasequence[i: i + len(subsequence)]
        if current_word == subsequence:
            current = 1
            
            # Loop through the DNA sequence, checking for additional occurrences
            # of the subsequence.
            for j in range(i + len(subsequence), len(dnasequence)
                           - len(subsequence) + 1, len(subsequence)):
                if dnasequence[j: j + len(subsequence)] != subsequence:
                    break # Exit the loop if the subsequence doesn't match.
                current += 1
            if maximum < current:
                maximum = current # Update the maximum occurrence count.
    return maximum

# Function to create a new profile (lists of longest repetition of each proteins).
def create_newprofile(proteins, sequence):
    newprofile = []
    for protein in proteins:
        numberOfProtein = count_sequence(sequence, protein)
        newprofile.append(numberOfProtein)
    return newprofile

# Function to read the unknown DNA sequence from a file.
def read_unknown_sequence(fileName): 
    text = open(fileName, 'r')
    
    # Read the first line from the file and remove leading/trailing whitespace.
    line = text.readline().strip()
    text.close()
    return line

def read_database():
    file = open('dna_db.csv', 'r')
    
    # Read and split the header row into a list of proteins.    
    proteins = file.readline().strip().split(',')

    # Remove the first element (header) which is not a protein name.
    proteins = proteins[1:]
    names = []
    numbers = []
    for line in file:
        line  = line.strip().split(',') # Split the current line by commas.
        names.append(line[0]) # The first element in each line is the name.

        # The rest of the elements are data related to protein occurrences.
        numbers.append(line[1:])
    file.close()
    return proteins, names, numbers 

# Function to convert a list of strings to a list of integers.  
def convert_to_integers(numbers):
    newnumbers = []
    for number in numbers:  
        newnumbers.append(int(number))
    return newnumbers

# Function to return name matching the profile.
def find_matching_person(names, numbers, newprofile):
    for i in range(len(numbers)):
        # Convert the data related to the current profile to integers.
        newnumbers = convert_to_integers(numbers[i])
        if newnumbers == newprofile:
            return ("Found match: " + names[i])
    return "No match"

def main():
    proteins, names, numbers = read_database()
    sequence = input("Sequence file: ")
    sequence = read_unknown_sequence(sequence)
    newprofile = create_newprofile(proteins, sequence)
    correctperson = find_matching_person(names, numbers, newprofile)
    print(correctperson)
if __name__ == "__main__":
    main()
