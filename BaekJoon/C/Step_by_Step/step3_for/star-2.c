#include <stdio.h>

int main (void)
{
    int N;
    int i;
    int j;

    scanf("%d", &N);

    for (i = 0; i < N; i++)
    {
        for (j = N - 1; j > i; j--)
        {
            printf(" ");
        }
        
        for (j = 0; j <= i; j++)
        {
            printf("*");
        }
         printf("\n");
    }
    
    return 0;

}