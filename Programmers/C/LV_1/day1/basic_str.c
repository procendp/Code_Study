#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool solution(const char* s) 
{
    int i;

    i = 0;
    while (s[i] != '\0')
    {
        if ((i == 3 || i == 5) && (s[i] >= '0' && s[i] <= '9'))
        {
             return true;
        }
        else
        {
            return false;
        }
        i++;
    }
}
    
/*
    for (i = 0; i >= s[i]; i++)
    {
        if (s[i])
        {
            
        }
        
    }
    strlen(s);
*/    

    // bool answer = true;
    //return answer;





