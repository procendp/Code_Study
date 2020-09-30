num = int(input())

for i in range(1, num + 1):
    print("*" * (num - i + 1))



# 출력 형식 잘못...?
# num = int(input())

# for i in range(num, 0, -1):
#     print('{:<6}'.format('*' * (i)))