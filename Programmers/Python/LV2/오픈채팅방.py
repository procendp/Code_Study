# Muzi in
# Prodo 
# Muzi out
# Prodo(Muzi) in
# Prodo -> Ryan
# -------------------> Prodo(Muzi), Ryan(Prodo) 둘 뿐.

def solution(record):
    answer = []
    userdict = {} # dictionary 추가

    for message in record: # Enter와 Change 들어온 경우 dictionary에 저장
        if (message.split(" ")[0] == "Enter") | (message.split(" ")[0] == "Change"):
            userdict[message.split(" ")[1]] = message.split(" ")[2] # 딕셔너리 쌍 추가하기
                                                                    # 자연스레 Muzi를 Prodo로 덮어씀
    for message in record:
        if message.split(" ")[0] == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(userdict[message.split(" ")[1]])) # 그 때마다 프린트
        elif message.split(" ")[0] == "Leave":
            answer.append("{0}님이 나갔습니다.".format(userdict[message.split(" ")[1]]))
        else:
            pass

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))


# def solution(record):
#     result = [] 
#     record_split = []
#     add = []

#     for i in range(len(record)):
#         record_split = record[i].split(" ")
#         result.append(record_split)
#         # return record_split

#     for j in range(len(record_split)):
#         if record_split[j][0] == "Enter":
#             add.append(record_split[j])


#     return add

# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]