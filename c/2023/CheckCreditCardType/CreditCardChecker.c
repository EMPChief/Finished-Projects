#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Print prompt to get credit card number from user
    printf("Enter your credit card number: ");

    // Declare a variable to store the credit card number
    long card_number;

    // Get credit card number from user, with validation to ensure it's not negative
    do
    {
        // Use get_long to obtain a long integer from the user
        card_number = get_long("Enter your credit card number: ");
    }
    while (card_number < 0);

    // Variables for sum and count to keep track of the algorithm
    int sum = 0;
    int count = 0;

    // Temporary variable to store the original card number for processing
    long temp = card_number;

    // Loop to process each digit of the card number
    while (temp > 0)
    {
        // Get the last digit of the card number
        int digit = temp % 10;

        // Check if the digit is at an even or odd position
        if (count % 2 == 0)
        {
            // If even, add the digit to the sum
            sum += digit;
        }
        else
        {
            // If odd, double the digit and add its digits to the sum
            int product = 2 * digit;
            sum += product % 10 + product / 10;
        }

        // Move to the next digit by dividing the temporary variable
        temp /= 10;

        // Increment the count to keep track of the position
        count++;
    }

    // Check if the sum is divisible by 10
    if (sum % 10 == 0)
    {
        // Check if the card number length and starting digits match AMEX
        if ((count == 15 || count == 16) && (card_number / 10000000000000 == 34 || card_number / 10000000000000 == 37))
        {
            // Print AMEX for American Express
            printf("AMEX\n");
        }
        // Check if the card number length and starting digits match MASTERCARD
        else if (count == 16 && (card_number / 100000000000000 == 51 || card_number / 100000000000000 == 52 ||
                                card_number / 100000000000000 == 53 || card_number / 100000000000000 == 54 ||
                                card_number / 100000000000000 == 55))
        {
            // Print MASTERCARD for MasterCard
            printf("MASTERCARD\n");
        }
        // Check if the card number length and starting digits match VISA
        else if ((count == 13 || count == 16) && (card_number / 1000000000000 == 4 || card_number / 1000000000000000 == 4))
        {
            // Print VISA for Visa
            printf("VISA\n");
        }
        // If it doesn't match any known card types, print INVALID
        else
        {
            printf("INVALID\n");
        }
    }
    // If the sum is not divisible by 10, print INVALID
    else
    {
        printf("INVALID\n");
    }

    // Return 0 to indicate successful program execution
    return 0;
}
