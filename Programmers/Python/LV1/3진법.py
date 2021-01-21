def solution(n):
    answer = []

    # 진법 변환 함수 만들기
    while True: 
        n, rest = divmod(n, 3) # n을 3으로 나눴을 시 몫, 나머지
        answer.append(rest)
        if n == 0:
            break
    
    return sum([3**idx * i for idx, i in enumerate(reversed(answer))])

print(solution(45))
print(solution(125))





# 흠..
    # answer.reverse() # [2, 1, 3]
    # # answer = "".join(map(str, answer)) #213

    # s = [] #2*4(0) + 1*4(1) + 3*4(2)
    # for i in range(len(answer)):
    #     a = int(answer[i]) * (rest ** i)
    #     s.append(a)
    # # s = sum(s)
    # return s