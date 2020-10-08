import datetime

def solution(a, b):

    date = 'Mon Tue WED THU FRI SAT SUN'.split()
    return date[datetime.date(2016, a, b).weekday()]

print(solution(5, 24))









# import datetime

# def solution(a, b):
#     date = 'MON TUE WED THU FRI SAT SUN'.split()

#     return date[datetime.datetime(2016, a, b).weekday()] # weekday() : 정수로 요일 반환. 월(0) 화(1) ... 일(6)

# print(solution(5, 24))



# 1월 1일 = 금요일
# 29일 - 2
# 30일 - 4 6 9 11
# 31일 - 1 3 5 7 8 10 12