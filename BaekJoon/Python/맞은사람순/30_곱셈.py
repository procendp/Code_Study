A = int(input())
B = int(input())

third = A * (B % 10)
fourth = A * ((B // 10) % 10)
fifth = A * (B // 100)
sixth = A * B

print(third)
print(fourth)
print(fifth)
print(sixth)