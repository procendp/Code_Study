def solution(n):
    
    binary_origin = bin(n) # 0b1001110
    origin_count = binary_origin.count('1') # n의 1 갯수 /// 4
    
    while True:
        n += 1
        binary_new = bin(n)
        new_count = binary_new.count('1')
        if origin_count == new_count:
            break
        return n

    # return n

print(solution(78))
print(solution(15))
print(solution(38))