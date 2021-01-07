from itertools import combinations

def prime_num(a, b, c):
    sum = a + b + c
    for i in range(2, sum): # 소수 판별
        if sum % i == 0:
            return False
    
    return True

def solution(nums):
    answer = 0
    
    lcomb = list(combinations(nums, 3))
    for i in lcomb:
        if prime_num(i[0], i[1], i[2]):
            answer += 1
    
    return answer




print(solution([1,2,3,4])) # 1 ..[1,2,4]
print(solution([1,2,7,6,4])) # 4.. [1,2,4] [1,4,6] [2,4,7] [4,6,7]








# def solution(nums):
#     answer = 0
#     sep = []

#     for i in range(len(nums)):
#         sep.append(nums[i])
#         if len(sep) == 3:
#             break


   

#     return sep