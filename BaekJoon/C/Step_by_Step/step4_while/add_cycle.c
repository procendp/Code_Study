#include <stdio.h>

int main (void)
{
    int N;      //입력 값
    int first;  //입력 값을 10으로 나눈 몫
    int rest;   //입력 값을 10으로 나눈 후 나머지
    int sum;    //몫 + 나머지
    int count;  //더한 값의 갯수

    first = N / 10;
    rest = N % 10;
    sum = first + rest;
    
    scanf("%d", &N);

    while (sum != N)
    {
        if()
        {

        }
        count++;
        printf("%d", count);
        break;
    }

}