def solution(n):
    new = []

    for i in range(n): 
        if i % 2 == 0: # 짝수라면
            new.append('수')
            
        else: # 홀수라면
            new.append('박')

    new = ''.join(new)
    
    return new

print(solution(3))
print(solution(4))