def solution(n, lost, reserve):
    array = []

    for i in range(n): # 리스트를 n개만큼 1로 초기화
        array.append(1)

    for k in range(len(reserve)):
        array[reserve[k] + 1] = 2

    for j in range(len(lost)): # lost 인덱스 값을 0으로 바꿔줌
        array[lost[j] - 1] = 0

    # if
    






    return array

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))

# 예제 #1
# 1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

# 예제 #2
# 3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.