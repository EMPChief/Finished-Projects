#include <stdio.h>
#include <stdlib.h>

// Function to print spaces based on a number
void printSpaces(int n);

// Function to print hash characters based on a number
void printHashes(int n);

int main(void)
{
    int height;
    char input[10];

    // Get the height of the pyramid from the user (1-8)
    do
    {
        printf("Enter the height of the pyramid (1-8): ");
        fgets(input, sizeof(input), stdin);
    }
    while (sscanf(input, "%d", &height) != 1 || height < 1 || height > 8);

    // Loop through each row to build the pyramid
    for (int row = 1; row <= height; row++)
    {
        // Print spaces before the left-side hashes
        printSpaces(height - row);

        // Print the left-side hashes
        printHashes(row);

        // Print two spaces between the sides
        printf("  ");

        // Print the right-side hashes
        printHashes(row);

        // Move to the next line for the next row
        printf("\n");
    }

    return 0;
}

// Function to print a specified number of spaces
void printSpaces(int n)
{
    // Loop to print spaces
    for (int i = 0; i < n; i++)
    {
        printf(" ");
    }
}

// Function to print a specified number of hash characters
void printHashes(int n)
{
    // Loop to print hashes
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
}
