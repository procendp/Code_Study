import math
def solution(n): # 121

    x = int(math.sqrt(n)) # 11
    
    if n == x**2:
        return (x+1)**2
    elif n != x**2:
        return -1

    return x

print(solution(121))
print(solution(3))