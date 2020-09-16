# 문제 예제
array = [1, 5, 2, 6, 3, 7, 4] # list 형태

i, j, k = input().split() # i = 2, j = 5, k = 3 .. i, j, k 입력받기.
i = int(i)
j = int(j)
k = int(k)

# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
ex1 = array[i-1:j] # index 1이상 5미만 [5, 2, 6, 3]
print(ex1)

# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
ex2 = sorted(ex1) # ex1 오름차순 정렬.. 
print(ex2)
                    ## ex1.sort()로 하면 None 반환.
                    ## sort는 정렬 된 목록을 반환하지 않는다. -> None
                    ## sorted(ex1) 해야 정렬된 목록을 반환한다.

# 2에서 나온 배열의 3번째 숫자는 5입니다.
ex3 = ex2[k-1] # k = 3 .. index = 2
print(ex3)