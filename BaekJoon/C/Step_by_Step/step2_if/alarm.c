#include <stdio.h>

int main (void)
{
    int h;
    int m;

    scanf("%d %d", &h, &m);

        if (h >= 1 && h <= 23)
        {
            if (m >=0 && m <= 44)
            {
                printf("%d %d", h - 1, m + 60 - 45);
            }
            else if (m >= 45 && m <= 59)
            {
                 printf("%d %d", h, m - 45);
            }
        }
        if (h == 0)
        {
            if (m >=0 && m <= 44)
            {
                printf("%d %d", h + 23, m + 60 - 45);
            }
            else if (m >= 45 && m <= 59)
            {
                 printf("%d %d", h, m - 45);
            }
        }
       
       return 0;

}