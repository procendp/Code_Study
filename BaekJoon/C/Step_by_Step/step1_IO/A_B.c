#include <stdio.h>

int main (void)
{
    int A;
    int B;

    scanf("%d %d", &A, &B);
    printf("%.9lf", (double)A/B);

    return 0;
}