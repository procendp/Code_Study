#include <stdio.h>

int main (void)
{
    int A;
    int B;

    while (scanf("%d %d", &A, &B) != EOF)
                                                /*EOF는 end of file로, 프로그램을 종료시킨다.
                                                이러한 EOF가 scanf를 만나면 -1로 입력되고, -1로 대신 사용해도 괜찮다.
                                                while문이 (1)을 담아 무한으로 돌고 있지 않을 때, 
                                                scanf 입력값을 제어함으로써 while문을 멈출 수 있다. 
                                                break ; 으로 while문을 멈추는 것과는 다름. */
    {
        printf("%d\n", A + B);
        
    }
    
    return 0;
}