import numpy as np

def solution(arr1, arr2):

    return (np.matrix(arr1) * np.matrix(arr2)).tolist()


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))



'''
1 4
3 2
4 1


3 3
3 3
'''


'''
2 3 2
4 2 4
3 1 4


5 4 3
2 4 1
3 1 1
'''