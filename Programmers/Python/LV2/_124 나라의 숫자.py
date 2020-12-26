# 다시


# 잘못품
def solution(n):
    answer = ""
    if n % 3 == 1:
        answer = "1"
        return answer

    elif n % 3 == 2:
        answer = "2"
        return answer

    elif n % 3 == 0:
        answer = "4"
        return answer

    return answer

print(solution(1)) # 1
print(solution(2)) # 2
print(solution(3)) # 4
print(solution(4)) # 11