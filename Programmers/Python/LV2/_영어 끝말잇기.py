def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]: # 뒤에 잘 연결되었는지 or 중복 있나
            
            return [(i % n) + 1, (i // n) + 1] # -번 사람, -번째 워드
    else:
        return [0,0]






print(solution(3, ["tank", "kick", "know",    "wheel", "land", "dream",    "mother", "robot", "tank"])) # [3,3]
print(solution(5, ["hello", "observe", "effect", "take", "either",   "recognize", "encourage", "ensure", "establish", "hang",   "gather", "refer", "reference", "estimate", "executive"])) # [0,0]
print(solution(2, ["hello", "one",   "even", "never",   "now", "world",   "draw"]))# [1,3]