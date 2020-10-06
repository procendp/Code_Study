N = int(input())
num = []
total = []
rest = (N % 5) % 3

if N % 5 == 0 or N % 3 == 0:
    if N % 5 == 0:
        num.append(N // 5)
        print(N % 5)

    elif rest == 0:
        num.append(int(N // 5))
        num.append(3**rest)
        num_list = list(map(int, num))
        total = sum(num_list)
        print(total)
    
    else:
        print(N // 3)
        
if N % 5 != 0 and N % 3 != 0:
    print(-1)




# 마지막 테케 11 해결 합시다..........





if N % 5 == 0 or N % 3 == 0:
    if N % 5 == 0:
        num.append(N // 5)
        num.append((N // 5) // 3)
        num_list = list(map(int, num))
        total = sum(num_list)
        print(total)
    elif N % 5 != 0:
        print(N // 3)


elif N % 5 != 0 and N % 3 != 0:
    print(-1)










# while N % 3 == 0 or N % 5 == 0:
#     num.append(N // 5)
#     num.append((N // 5) // 3)
#     num_list = list(map(int, num))
#     total = sum(num_list)

#     break

# if N % 3 != 0 or N % 5 != 0:
#         num.append(-1)
#         num_list = list(map(int, num))
#         total = sum(num_list)

# print(total)