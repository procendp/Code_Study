def solution(arr, divisor):
    new = []
        
    for i in range(0, int(len(arr))): # 0,1,2,3 돌고
        if (arr[i] % divisor == 0):
            new.append(int(arr[i]))
            new.sort()
    if (arr[i] // divisor == 0):
        new.append(-1)

    return new

print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3,2,6], 10))



