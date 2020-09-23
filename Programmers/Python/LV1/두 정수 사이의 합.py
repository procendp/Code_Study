def solution(a, b):
    answer = 0
    if a < b:
        answer = (b*(b+1)//2) - ((a-1)*(a)//2)
    elif a == b:
        answer = a
    elif a > b:
        answer = (a*(a+1)//2) - ((b-1)*(b)//2)

    return answer

print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))