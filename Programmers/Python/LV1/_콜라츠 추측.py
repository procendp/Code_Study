def solution(num): # 테스트5만 실패
    
    count = 0
    while num != 1: # 주어진 수가 1이 될 때까지
        if num % 2 == 0: # 주어진 수가 짝수면
            num = (num / 2)
            count += 1
        elif num % 2 == 1: # 주어진 수가 홀수면
            num = (num * 3) + 1
            count += 1
        if count >= 500:
                return -1
        elif num == 1:
            break
    
    return count

print(solution(6))
print(solution(16))
print(solution(626331))

# def solution(num): # 테스트5만 실패
    
#     count = 0
#     while num != 1 and count < 500: # 주어진 수가 1이 될 때까지
#         if num % 2 == 0: # 주어진 수가 짝수면
#             num = (num / 2)
#             count += 1
#         elif num % 2 == 1: # 주어진 수가 홀수면
#             num = (num * 3) + 1
#             count += 1
        
#     return count < 500 and count or -1 # count 참 , -1 거짓