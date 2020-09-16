#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) 
{
    int i;
    int answer = 0;

    for (i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            answer += i;
        }
    }

    //return answer;
}

int main (void)
{
    int a;
    a = solution(12);
    printf("%d", a);
    return 0;
}