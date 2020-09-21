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
# for i in range(0, int(len(numbers))): # 1칸
#     new.append(int(numbers[i-1]) + int(numbers[i]))

# for i in range(0, int(len(numbers))): # 2칸
#     new.append(int(numbers[i-2]) + int(numbers[i]))

# for i in range(0, int(len(numbers))): # 3칸
#     new.append(int(numbers[i-3]) + int(numbers[i]))

# for i in range(0, int(len(numbers))): # 4칸
#     new.append(int(numbers[i-1]) + int(numbers[i]))
# new = []
# numbers = [1, 2, 3]
# i = int(len(numbers))
# while i >= 0:
#     for i in range(int(len(numbers)), 0): # 1칸
#         new.append(int(numbers[i]) + int(numbers[i+1]))

    
#         i -= 1
#     break
# new.sort()
# new = list(set(new))
#     # return new

# print(new)