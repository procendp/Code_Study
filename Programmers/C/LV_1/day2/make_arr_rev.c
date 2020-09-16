#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(long long n) {

    int* answer = null;//(int*)malloc(...);
    int rest;
    int arr;
    int count;

    count = 1;
    rest = 0;
    while (n != 0)
    {
        rest = (int)(n % 10); // long long n을 int형으로 형변환 해야하고, 나머지 전체를 형변환해야함.
        
        for (int i = count - 1; i < count; i++)
        {
            arr[i] = rest;
        }
        
        count++;
        n = n / 10;
    }
    answer = count;
    
    return answer;
}

int main (void)
{
    printf("%d", solution(12345));
    return 0;
}