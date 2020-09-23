def solution(s):
    answer = True
    if s.lower().count('p') == s.lower().count('y'):
        return answer
    else:
        return False

print(solution("pPoooyY"))
print(solution("Pyy"))

# 블로그
# def solution(s):
#     return s.lower().count('p') == s.lower().count('y')           # p, y가 모두 하나도 없는 경우는 갯수가 0으로 같으므로 True를 리턴하니까 굳이 안써줘도 됨.

# print(solution("pPoooyY"))
# print(solution("Pyy"))