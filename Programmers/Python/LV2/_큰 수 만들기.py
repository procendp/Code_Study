def solution(number, k):
    answer = list(map(int, number))
    answer.sort()
    for i in range(len(answer)):
        del answer[k:len(answer)]


    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))