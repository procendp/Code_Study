def solution(land):

    maximum0 = max(land[0]) # 5
    idx0 = land[0].index(max(land[0])) # index 3
    reject1 = land[1].pop(idx0)

    maximum1 = max(land[1]) # 7
    idx1 = land[1].index(max(land[1])) # index 2
    reject2 = land[1].pop(idx1)

    maximum2 = max(land[2]) # 4
    idx2 = land[2].index(max(land[2])) # index 0

    

    return maximum0 + maximum1 +  maximum2


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))  # 16