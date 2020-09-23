def solution(s):
    answer = ''
    if len(s) % 2 == 1: # 홀수라면
        answer = s[len(s)//2]
        return answer
    
    else: # 짝수라면
        answer = s[(len(s)//2)-1:(len(s)//2)+1] # [3:5] ... 3~4번째 인덱스
        return answer

    
print(solution("abcde"))
print(solution("qwer"))

# 01234567 짝수..8개
# xxx00xxx ...4,5번째