a, b = map(int, input().strip().split(' ')) # a : 가로 길이, b : 세로 길이, .strip() : 문자열 양 끝 공백과 개행 삭제
for i in range(0, b):
    for j in range(0, a):
        print("*", end='')  # end='' : 다음 출력이 바로 뒤에 붙음. *****
    print() # 개행
    



# int main(void) 
# {
#     int a; //가로 길이
#     int b; //세로 길이
#     int i;
#     int j;
    
#     scanf("%d %d", &a, &b);

#     for (i = 0; i < b; i++)
#     {
#         for (j = 0; j < a; j++)
#         {
#             printf("*");
#         }
#         printf("\n");
#     }

#     return 0;
# }