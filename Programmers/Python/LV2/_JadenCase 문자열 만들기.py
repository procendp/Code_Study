def solution(s):
    answer = ''
    s = s.lower()
    delete = s.replace(s[0], '') # s[0] = 3

    # if s[0][0].isdigit() == True:
    #     return s[0] + delete.title()

    # else:
    #     return s.title()

    return s[0]

print(solution("3people unFollowed me"))
print(solution("for the last week"))







# def solution(s):
#     answer = ''
#     s = s.lower()

#     spl = s.split(" ")

#     for i in spl:
#         i = i.capitalize()
#         answer += i + " "


#     return answer[:-1]

# print(solution("3people unFollowed me"))
# print(solution("for the last week"))


# 숫자 없을 땐
# return s.title()만 해도 됨   ..> title()은 각 공간 직후 문자를 대문자로 만들어줌.
