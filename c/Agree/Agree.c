#include <stdio.h>
#include <string.h>
#include "cs50.h"

int main(void)
{
    char c[4];

    printf("Do you agree? ");
    scanf("%s", c);

    if (strcmp(c, "y") == 0 || strcmp(c, "Y") == 0 || strcmp(c, "yes") == 0 || strcmp(c, "Yes") == 0 || strcmp(c, "YES") == 0)
    {
        printf("So you do agree\n");
    }
    else if (strcmp(c, "n") == 0 || strcmp(c, "N") == 0 || strcmp(c, "no") == 0 || strcmp(c, "No") == 0 || strcmp(c, "NO") == 0)
    {
        printf("So you don't agree\n");
    }
    else
    {
        printf("Invalid\n");
    }

    return 0;
}
