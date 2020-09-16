#include <stdio.h>

int main (void)
{
    int i;
    int N;

    scanf("%d", &N);

    for (i = N; i >= 1; i--)
    {
        printf("%d\n", i);
    }
    
    return 0;
}