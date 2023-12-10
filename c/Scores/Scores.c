#include <stdio.h>
#include "cs50.h"

int main(void)
{
    // Declare a variable to store the number of scores
    int n;

    // Use a do-while loop to ensure a valid number of scores is entered
    do
    {
        number = get_int("Type how many scores you want to use: ");
    } while (n <= 0);

    // Declare an array to store the scores based on the user-specified number
    int scores[n];

    // Use a for loop to input the scores based on the specified number
    for (int i = 0; i < n; ++i)
    {
        scores[i] = get_int("Score number: ");
    }

    // Initialize a variable to store the sum of the scores
    float sum = 0;

    // Use a for loop to calculate the sum of the scores
    for (int i = 0; i < n; ++i)
    {
        sum += scores[i];
    }

    // Calculate and print the average school grade
    printf("Average school grade is: %f\n", sum / (float)n);

    // Indicate successful completion of the program
    return 0;
}
