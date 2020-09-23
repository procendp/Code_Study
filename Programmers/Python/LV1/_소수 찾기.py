def solution(n):
    length = []
    for i in range(1, n+1): # len(n)
        for j in range(1,n):
            if i % j == 0:
                length.append(i)

    return length 

print(solution(10))
print(solution(5))

# 1부터 n까지 계산하게 돌린다.. i
# 1이면 1, 2면 2, 3이면 3... n이면 n까지 나누게 돌린다... j
# 그 때의 길이를 담고,
# 그 길이가 2라면 answer에 담는다.

#  length = []                          ...n의 약수 구하기.
#     for i in range(1, n+1): # len(n)
#         if n % i == 0:
#             length.append(i)




# 에라토스테네스의 체
# --------------------------------------------
# def solution(n):
#     num=set(range(2,n+1))
#     for i in range(2,n+1):
#         if i in num:
#             num -=set(range(2*i,n+1,i))
#     return len(num)