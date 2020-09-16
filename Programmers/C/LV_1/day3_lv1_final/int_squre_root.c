#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h> //sqrt() 쓰려면 추가해줘야하고

long long solution(long long n)
{
    long long answer = 0;
    long x = sqrt(n); //sqrt는 괄호 안 변수의 제곱근이다. 즉, n이 121이면 x는 11.

    if (n == x*x)
    {
        return (x + 1)*(x + 1);
    }
    else if (n != x*x)
    {
        return -1;
    }

    return answer;
}