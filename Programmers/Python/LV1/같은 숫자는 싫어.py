def solution(arr):
    for i in range(1, int(len(arr))):
    if arr[i] != arr[i-1]:
        new.append(arr[i])

    else :
        continue

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))

# arr = [4,4,4,3,3]
# new = []
# new.append(arr[0])
# new2 = []
# for i in range(1, int(len(arr))): # [1, 3, 3, 0, 0, 1]
#     if arr[i] != arr[i-1]:
#         new.append(arr[i])

#     else :
#         continue


# print(new)