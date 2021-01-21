def solution(a, b):
    total = []

    for i in range(len(a)):
        total.append(a[i] * b[i])

    return sum(total)

print(solution([1,2,3,4], [-3,-1,0,2])) # 3
print(solution([-1,0,1], [1,0,-1])) # -2