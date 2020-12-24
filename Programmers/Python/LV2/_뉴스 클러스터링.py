# def solution(str1, str2):
#     answer = 0

#     str1.upper()
#     str2.upper()

#     if str1 == str2:
#         return 65536

#     # cut1 = []
#     # cut2 = []

#     # length = 2
#     # cut1 = map(''.join, zip( * [iter(str1)] * length))
#     # cut2 = map(''.join, zip( * [iter(str2)] * length)) # 문자열 2개씩 자르기






#     return answer


# print(solution("FRANCE", "french")) # 16384
# print(solution("handshake", "shake hands")) # 65536
# print(solution("aa1+aa2", "AAAA12")) # 43690
# print(solution("E=M*C^2", "e=m*c^2")) # 65536



# 자카드 유사도
# 집합 A, B
# J(A, B) = 교집합/합집합 ex) 2/4
# 두 집합 공집합일 경우 J(A, B) = 1



import collections

def solution(str1, str2):
    arr1, arr2 = list(), list()
    for i in range(max(len(str1), len(str2))-1):
        if (str1[i:i+2].isalpha()) and (len(str1[i:i+2]) == 2): 
            arr1.append(str1[i:i+2].lower())
        if (str2[i:i+2].isalpha()) and (len(str2[i:i+2]) == 2): 
            arr2.append(str2[i:i+2].lower())

    counter1, counter2 = collections.Counter(arr1), collections.Counter(arr2)
    intersection, union = counter1 & counter2, counter1 | counter2

    sum1, sum2 = sum(x[1] for x in intersection.items()), sum(x[1] for x in union.items())

    if sum2 == 0:
        return 65536

    else:
        return (65536*sum1) // sum2


print(solution("FRANCE", "french")) # 16384
print(solution("handshake", "shake hands")) # 65536
print(solution("aa1+aa2", "AAAA12")) # 43690
print(solution("E=M*C^2", "e=m*c^2")) # 65536
