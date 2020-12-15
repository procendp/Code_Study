# 다시






# def solution(arr):
#     arr.sort()
    
#     answer = max(arr)

#     while True:
#         for i in range(len(arr) - 1):
#             if answer % arr[i] != 0:
#                 break

#         else:
#             return answer
#         answer += max(arr) # n만큼 더해줌, 즉, n배 곱


# print(solution([2,6,8,14]))
# print(solution([1,2,3]))


































# rererere
# def solution(arr):
#     answer = []

#     arr.sort()

#     for i in range(len(arr)):
#         if max(arr) % arr[i] == 0:
#             print(max(arr))

#         # else:
#             # max(arr)를 n만큼 곱해서 증가시킨다. 다른 원소가 나눠떨어질 때까지.
      
#     return answer


# print(solution([2,6,8,14]))
# print(solution([1,2,3]))




# 최소공배수
# n1 = 4
# n2 = 14


# for i in range(n2, (n1 * n2) + 1):
#     if i % n1 == 0 and i % n2 == 0:
#         print(i)
#         break