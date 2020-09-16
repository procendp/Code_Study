#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n)
{
    int answer = 0;
    int rest;

    rest = 0;
    while (n != 0)
    {
        rest = n % 10;
        answer += rest;
        n = n/10;
    }

    return answer;
}

// int main (void)
// {
//     printf("%d", solution(42));
//     return 0;
// }