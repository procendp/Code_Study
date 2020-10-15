N = int(input())
M = list(map(int, input().split()))
max_M = max(M)

for i in range(N):
    M[i] = M[i]/max_M*100

avg = sum(M) / N
print("{0}".format(avg))