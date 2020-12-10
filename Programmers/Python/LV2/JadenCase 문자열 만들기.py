def solution(s):
    answer = ''
    s = s.lower()

    spl = s.split(" ")

    for i in spl:
        i = i.capitalize()
        answer += i + " "


    return answer[:-1]

print(solution("3people unFollowed me"))
print(solution("for the last week"))
