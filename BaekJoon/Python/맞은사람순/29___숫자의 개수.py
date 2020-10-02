A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
mul_list = list(str(mul)) # ['1', '8', '6', '0', '8', '6', '7']

print(mul_list.count('0'))
print(mul_list.count('1'))
print(mul_list.count('2'))
print(mul_list.count('3'))
print(mul_list.count('4'))
print(mul_list.count('5'))
print(mul_list.count('6'))
print(mul_list.count('7'))
print(mul_list.count('8'))
print(mul_list.count('9'))

# print문을 for문으로 줄이고 싶은데..