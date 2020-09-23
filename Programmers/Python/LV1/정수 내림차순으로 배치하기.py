def solution(n):
    answer = int(''.join(sorted(str(n), reverse=True))) 
                # str(n) : str로 주어진 정수->문자열 형변환 /rev : 내림차순 /''.join(sorted()) : 리스트를 문자열로 변환 -> 이후 int로 변환
    return answer

print(solution(118372))