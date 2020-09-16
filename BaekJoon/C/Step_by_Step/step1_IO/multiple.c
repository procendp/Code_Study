#include <stdio.h>

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b); //1,2번 입력
    
    //출력값
    //3번 출력
    printf("%d\n", a*(b%10) );
    //4번 출력
    printf("%d\n", a*(((b-(b%10))%100)/10) );
    //5번 출력
    printf("%d\n", a*((b-(b%100))/100));
    //6번 출력
    printf("%d\n", a*b );
    
    return 0;   
}
