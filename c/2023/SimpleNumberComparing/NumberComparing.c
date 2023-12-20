#include <stdio.h>
#include "cs50.h"

int main(void)
{
    int a = get_int("What is the a?");
    int b = get_int("What is the b?");

    if (a > b)
    {
        printf("a is bigger than b\n");
    }
    else if (a < b)
    {
        printf("a is less than b\n");
    }
    else
    {
        printf("a and b are equal\n");
    }

    return 0;
}
