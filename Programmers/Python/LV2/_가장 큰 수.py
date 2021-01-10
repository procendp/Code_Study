# 다시
def solution(numbers):
    numbers = list(map(str, numbers)) # int(numbers) -> str
    somelist = []

    for i in range(len(numbers)):
        somelist.append(numbers[i] + numbers[i-1])


    return somelist

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))



# def solution(numbers):

#     numbers = list(map(str, numbers))
#     numbers.sort(key= lambda x : x*3, reverse= True)

#     answer = "".join(map(str, numbers))

#     return answer


# print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))





# aaa = numbers[:]    -> numbers의 첨부터 끝까지를 넣어준다.