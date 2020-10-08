def solution(n):
    n = list(str(n))        # ['1', '2', '3', '4', '5']  .. int -> list(str)
    n.reverse()             # ['5', '4', '3', '2', '1']
    n = list(map(int, n))   # [5, 4, 3, 2, 1]            .. list(str) ->  list(int)

    return n

print(solution(12345))



# 블로그 1
# def solution(n):
# 	return [int(i) for i in str(n)][::-1]    # [::-1] : 배열 뒤집기

# 블로그 2
# def solution(n):
# 	return list(map(int, reversed(str(n))))