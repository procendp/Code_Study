def solution(phone_number):

    num = phone_number[-4:]
    answer = '*'*(len(phone_number)-4) + num
    return answer

print(solution("01033334444"))
print(solution("027778888"))


# import re
# def solution(phone_number):
    
#     aaa = re.sub(phone_number[:-4], '*', phone_number)
#     answer = '*'*(len(phone_number)-5) + aaa
#     return answer