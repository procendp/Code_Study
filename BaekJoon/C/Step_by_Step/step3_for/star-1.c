#include <stdio.h>

int main (void)
{
    int N;
    int i;
    int j;

    scanf("%d", &N);

    for (i = 1; i <= N; i++)
    {
        for (j = 1; j <= i; j++)
        {
            printf("*");
        }
         printf("\n");
    }
    
    return 0;

}