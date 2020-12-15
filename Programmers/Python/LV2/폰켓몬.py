def solution(nums):
    answer = 0
    nums_setlist = list(set(nums))    # 집합으로 중복 제거 후 다시 리스트화

    if len(nums_setlist) > len(nums) // 2:
        answer = len(nums) // 2

    else:
        answer = len(nums_setlist)

    return answer

print(solution([3,1,2,3]))      # 2
print(solution([3,3,3,2,2,4]))  # 3
print(solution([3,3,3,2,2,2]))  # 2