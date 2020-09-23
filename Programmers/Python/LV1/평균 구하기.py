def solution(arr):
    new = sum(arr)
    answer = new / len(arr)

    return answer

print(solution([1,2,3,4]))
print(solution([5,5]))