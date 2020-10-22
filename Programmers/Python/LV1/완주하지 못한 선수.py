def solution(participant, completion):
    participant.sort() 
    completion.sort() 

    for i in range(len(completion)): 
        if participant[i] != completion[i]: 
            return participant[i] 
            
    return participant[i + 1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))










# a_sub_b = [x for x in a if x not in b]
# answer = [x for x in participant if x not in completion]    # 리스트 빼기 리스트

   
    # for i in range(len(participant)):
    #     if participant[i] == participant[i-1]:
    #         answer.append(participant[i])