def solution(numbers):
    new = []

    for i in range(0, int(len(numbers))):
        for j in range(1, int(len(numbers)-1)):
            new.append(int(numbers[i-j]) + int(numbers[i]))
            
    new = list(set(new))
    new.sort()
    return new

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))
print(solution([1,2,3]))
print(solution([7,3]))

### 더 간단히

# def solution(numbers):
#     new = set()

#     for i in range(0, int(len(numbers))):
#         for j in range(1, int(len(numbers)-1)):
#             new.add(int(numbers[i-j]) + int(numbers[i]))
            
#     return sorted(new)