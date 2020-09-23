def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit(): # .isdigit() : 문자열이 숫자로만 이루어져 있는지 확인
        return True
    else:
        return False

print(solution("a234"))
print(solution("1234"))