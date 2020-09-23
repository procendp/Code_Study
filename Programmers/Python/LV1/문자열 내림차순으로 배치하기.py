def solution(s):
    answer = ''
    answer = ''.join(sorted(s, reverse=True)) # ''.join 함으로써 리스트를 문자열로 만든다.
    
    return answer

print(solution("Zbcdefg"))