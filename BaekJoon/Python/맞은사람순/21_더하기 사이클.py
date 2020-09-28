N = N2 = int(input()) #26

count = 0
while True:
    tens = N // 10
    ones = N % 10
    sumsum = tens + ones
    count += 1
    N = int(str(N % 10) + str(sumsum % 10))
    if N == N2:
        break

print(count)






##26
# 2 + 6 = 8 #68
#     6 + 8 = 14 #84
#         8 + 4 = 12 #42
#             4 + 2 = 6 #26
                