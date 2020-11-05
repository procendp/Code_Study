def solution(s): #str은 list로 일일이 나눠주지 않아도 반복문 가능

    stack = []    
    for i in range(len(s)):
        if s[i] == '(': # '(' 라면 stack에 저장
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0: # stack에 ')'만 남음, 따라서 False
                return False
            stack.pop() # ')' 라면 stack에 있는 거 뺌

    if len(stack) != 0: # stack에 뭐라도 남아있다면 False
            return False

    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))