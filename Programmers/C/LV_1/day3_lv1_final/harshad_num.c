#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x)
{
	bool answer = true;

    int temp = x;
    int sum = 0;

    while (x != 0) // while (x)와 같다.
    {
    	sum = sum + (x % 10);
        x = x / 10;
    }
    if (temp % sum != 0)
    {
        answer = false;
    }
    
    return answer;
}
/*
int main (void)
{
    solution(13);
    return 0;
}
*/