def solution(A,B):
    stacked = []
    
    A.sort() # 1 2 4
    B.sort(reverse=True) # 5 4 4

    for i in range(len(A)):
        stacked.append(A[i] * B[i])
    
    return sum(stacked)



print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1,2], [3,4]))

# A의 가장 큰 수를 B의 가장 작은 수랑 곱하고 뺀다.
# A는 오름차순, B는 내림차순
