def solution(n):
    jmp = 0
    while(n):
        ans = n % 2
        if ans == 1:
            jmp += 1
            n -= 1
        else:
            n = n // 2

    return jmp
    



print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5



# 건전지 사용량 최소로 하기
# k칸 점프 - 건전지 사용량 k
# 순간이동 - 현재까지 온 거리 x2
