def solution(n):
    new = str(n)
    answer = 0
    for i in range(len(new)):
        answer += int(new[i])

    return answer

print(solution(123))
print(solution(987))