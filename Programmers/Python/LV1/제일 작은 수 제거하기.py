def solution(arr): # 제일 작은 수 
    minimum = min(arr)
    arr.remove(minimum)

    if not arr:
        arr.append(-1)

    return arr

print(solution([4,3,2,1]))
print(solution([10]))