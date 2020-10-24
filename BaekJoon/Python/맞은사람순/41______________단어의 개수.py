sentence = input()

space = sentence.count(" ")

if sentence[0] == " " or sentence[-1] == " ":
    print(space)

else:
    print(space + 1)



# 뭐가 문제지..