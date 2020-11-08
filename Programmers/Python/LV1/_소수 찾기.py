# 재도전
def solution(n):
    array = []
    some = []
    for i in range(1, n+1): # len(n)
        array.append(i)     # [1, 2, 3, 4, 5]
    array.remove(array[0])  # [2, 3, 4, 5]  # 1 본인 제외


    for j in range(0, len(array)):
        # print(j)        # 0  1  2  3
        # print(array[j]) # 2, 3, 4, 5
        
        # 약수
        for k in range(1, j):
            if array[j] % k == 0:
                some.append(array[j])


    return some

# print(solution(10))
print(solution(5))





# 에라토스테네스의 체
# --------------------------------------------
# def solution(n):
#     num=set(range(2,n+1))
#     for i in range(2,n+1):
#         if i in num:
#             num -=set(range(2*i,n+1,i))
#     return len(num)