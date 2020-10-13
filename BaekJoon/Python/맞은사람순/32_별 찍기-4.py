num = int(input())

for i in range(num, 0, -1):
    print(" " * (num - i) + "*" * i)


# 뭐가 또..
# star = int(input())
# for i in range(star+1, 1, -1):
#     print('{:>5}'.format('*' * (i-1)))