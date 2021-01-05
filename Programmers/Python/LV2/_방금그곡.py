def solution(m, musicinfos):
    answer = ''
    sound = "C, C#, D, D#, E, F, F#, G, G#, A, A#, B"

    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "HELLO"
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])) # "FOO"
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])) # "WORLD"
# 추가 테스트 케이스
print(solution("A#",["23:56,00:00,HAPPY,B#A#"])) #happy
print(solution("CDEFGAC",["12:00,12:06,HELLO,CDEFGA"])) #none
print(solution("CCB",["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"])) #foo