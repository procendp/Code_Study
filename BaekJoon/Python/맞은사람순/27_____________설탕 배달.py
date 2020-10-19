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



# 다른 풀이
# def sugar(N) :
#     for y in range( (N//3)+1) :
#         for x in range( (N//5)+1 ) :
#             if ((5*x + 3*y) == N) :
#                 return x+y
            
#     return -1

# N = int(input()) #배달해야할 설탕 킬로그램         
# print(sugar(N))