def solution(n):
    new = []
    for i in range(1, int(n)+1):
        if n % i == 0:
            new.append(i)
            
        else:
            continue
    return sum(new)

print(solution(12))
print(solution(5))