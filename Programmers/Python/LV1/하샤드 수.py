def solution(x):

    sum = 0
    for i in str(x):
        sum += int(i)
        
    if x % sum:
        return False
    else:
        return True



print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))