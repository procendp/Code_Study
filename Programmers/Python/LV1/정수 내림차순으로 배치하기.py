def solution(n):
    answer = int(''.join(sorted(str(n), reverse=True)))
    return answer

print(solution(118372))