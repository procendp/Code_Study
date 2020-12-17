def solution(n):

    nbinary = bin(n)
    bcnt = nbinary.count('1')
    
    for i in range(n+1, 1000001):
        if bin(i).count('1') == bcnt:
            return i


print(solution(78))
print(solution(15))
print(solution(38))