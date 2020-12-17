# 다시

def solution(s):
    a, b = 0, 0

    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]

    return [a, b]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))















# 다시
