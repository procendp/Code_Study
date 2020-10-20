def solution(participant, completion):
    # a_sub_b = [x for x in a if x not in b]
    answer = []
    # for i in range(0, len(participant)):
    #     for j in range(0, len(completion)):
    #         if participant[i] == completion[j]:
    #             answer.append(participant[i])   
    
    # answer = participant + completion
    # answer = set(answer)
    
    for i in range(len(participant)):
        if participant[i] == participant[i-1]:
            answer.append(participant[i])
    
    answer = [x for x in participant if x not in completion]    # 리스트 빼기 리스트
    
    return answer

    # answer = list(set(participant).intersection(completion))
    # return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))