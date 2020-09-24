def solution(participant, completion):
    # a_sub_b = [x for x in a if x not in b]
    answer = []
    # for i in range(0, len(participant)):
    #     for j in range(0, len(completion)):
    #         if participant[i] == completion[j]:
    #             answer.append(participant[i])   
    
    # answer = participant + completion
    # answer = set(answer)
    answer = [x for x in participant if x not in completion]    # 리스트 빼기 리스트

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))