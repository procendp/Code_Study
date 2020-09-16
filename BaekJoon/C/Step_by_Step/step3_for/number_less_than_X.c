#include <stdio.h>

int main (void)
{
    int N;
    int A;
    int X;
    int i;

    scanf("%d %d", &N, &X);
    
    for (i = 1; i <= N; i++)
    {
        scanf("%d", &A);

        if (A < X)
        {
            printf("%d ", A);
        }
    }

    return 0;    
}