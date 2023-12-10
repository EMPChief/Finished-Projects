// add the library
#include <cs50.h>
#include <stdio.h>

// initialize the program
int main(void)
{
    // prompts the user to enter starting population
    int starting_size;
    do
    {
        starting_size = get_int("Input an int for starting size: (must be greater or equal to 9) ");
    }
    while (starting_size < 9);

    // prompt the user for ending size
    int ending_size;
    do
    {
        ending_size = get_int("Input ending population: (must be equal or higher than starting number) ");
        // check if ending size is less than starting size and reject the input
        if (ending_size < starting_size)
        {
            printf("Ending size must be equal or higher than starting size. Please try again.\n");
        }
    }
    while (ending_size < starting_size);

    // calculate the amount of years
    int years = 0;

    // while loop for population growth
    while (starting_size < ending_size)
    {
        starting_size = starting_size + (starting_size / 3) - (starting_size / 4);
        years++;
    }

    // prints the answer out
    printf("Years: %d\n", years);

    return 0;
}
