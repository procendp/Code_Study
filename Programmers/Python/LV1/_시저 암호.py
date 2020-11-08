# 다시 풀어보자
def solution(s, n):
    s = list(s) # 리스트 자르기
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr(((ord(s[i]) - ord('A') + n) % 26) + ord('A'))
        elif s[i].islower():
            s[i] = chr(((ord(s[i]) - ord('a') + n) % 26) + ord('a'))

    return "".join(s)

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))

# ord() : ord(문자) -> ascii
# chr() : chr(ascii) -> 문자

# ascii
# A-Z : 65 - 90
# a-z : 97 - 122

# 문자열 한글자씩 자르기 : aaa = list(str)

# 블로그
# def solution(s, n): 
#     s = list(s) 
#     for i in range(len(s)): 
#         if s[i].isupper(): 
#             s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A')) 
#         elif s[i].islower(): s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a')) 
#     return "".join(s)
