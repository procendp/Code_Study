def solution(array, commands):
    answer = []
    new = []
    for i in range(len(commands)):
        new = array[commands[i][0]-1:commands[i][1]] 
        new.sort()
        
        answer.append(new[commands[i][2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))




 # for i in range(0, int(len(array))-1):
    #     a = int(commands[i][0])
    #     b = int(commands[i][1])
    #     c = int(commands[i][2])

    #     array = array[a-1:b] # index 1-4
    #     array.sort()
        
    #     answer.append(array[int(c-1)]) # 5





 # 블로그 
    # answer = []
    # for oned in commands: # commands 원소의 인덱스를 이용해 array 슬라이싱하기.
    #     new = array[oned[0]-1:oned[1]] # oned : 1차원배열로 []라고 생각하면 됨... 따라서, oned[0]은 [][0] == commands[n번째][0]
    #     new.sort()
    #     answer.append(new[oned[2]-1])