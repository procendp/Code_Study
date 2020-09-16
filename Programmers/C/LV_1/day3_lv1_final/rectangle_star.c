#include <stdio.h>

int main(void) 
{
    int a; //가로 길이
    int b; //세로 길이
    int i;
    int j;
    
    scanf("%d %d", &a, &b);

    for (i = 0; i < b; i++)
    {
        for (j = 0; j < a; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}