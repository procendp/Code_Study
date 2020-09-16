#include <stdio.h>

int main (void)
{
    int A;
    int B;

    while (1)
    {
        scanf("%d %d", &A, &B);
        if (A + B == 0)
        {
            break;
        }
        
        printf("%d\n", A + B);
    }
    
    return 0;
}