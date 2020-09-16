#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(long long num)
{
    int answer = 0;
    int count = 0;

    while (num != 1)
    {
        if(num % 2 == 0)
        {
            num = num / 2;
            count++;
        }
        else if(num % 2 == 1)
        {
            num = (3 * num) + 1;
            count++;
        }
        if (count > 500)
        {
            return -1;
        }
    }
    return count;

    return answer;
}

int main (void)
{
    solution(6);
    return 0;
}