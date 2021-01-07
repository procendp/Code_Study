def solution(people, limit):
    answer = 0
    people.sort() # [50, 50, 70, 80]
    some = []

    if people[0] + people[-1] > limit:
        some.append(people[-1])
        # people.pop(people[-1])








    return people




print(solution([70, 50, 80, 50], 100)) # 3
# print(solution([70, 80, 50], 100)) # 3