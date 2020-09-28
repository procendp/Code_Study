# 내 풀이
A, B, C = map(int, input().split())
temp = 0

if A < B:
    temp = A
    A = B
    B = temp

if B < C:
    temp = B
    B = C
    C = temp

if A < B:
    temp = A
    A = B
    B = temp

# if C < A:
#     temp = C
#     C = A
#     A = temp

print(B)


# 블로그
# A, B, C = map(int, input().split())
# List = list()
# List.append(A)
# List.append(B)
# List.append(C)

# List.sort()
# print(List[1])