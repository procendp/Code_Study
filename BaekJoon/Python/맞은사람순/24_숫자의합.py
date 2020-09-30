N = input()
num = input()
num_list = list(num)
int_num_list = list(map(int, num_list))

total = sum(int_num_list)
    
print(total)

# 리스트 문자열을 숫자로 전환 ['5', '4', '3'] ....> [5, 4, 3]
# num_list = list(map(int, num_list))