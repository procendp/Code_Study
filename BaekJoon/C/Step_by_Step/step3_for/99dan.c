#include <stdio.h>

int main(void)
{
    int i;
    int j;

    scanf("%d", &i);
    
    for (j = 1; j <= 9; j++)
        {
            printf("%d * %d = %d\n", i, j, i*j); 
        }
        j++;

    return 0;
}