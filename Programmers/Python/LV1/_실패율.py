def solution(N, stages): # N : 전체 스테이지의 개수, stages : 유저가 현재 멈춰있는 스테이지의 번호가 담긴 배열
    
    done_user = len(stages)             # 스테이지에 도달한 플레이어 수
    rate = []                           # 실패율 = cant / done_user

    for i in range(1, N+1):
        cant = 0                        # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        for j in range(done_user):
            if stages[j] == i:
                cant += 1
        if cant == 0:
            rate.append(0)
        else:
            rate.append(cant/done_user)
        done_user -= cant
    
    a = sorted(rate, reverse=True)
    result = []

    for i in range(len(a)):
        result.append(rate.index(a[i])+1)
        rate[rate.index(a[i])] = 2

    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))