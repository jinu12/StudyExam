# 소수 찾기 1
# from sys import stdin
# cnt1 = 0
# cnt2 = 0
# N = int(stdin.readline())
# A = stdin.readline().split()
# X = list(int(A[i]) for i in range(N))
# for i in range(len(X)):
#     for j in range(1, X[i] + 1):
#         if X[i] % j == 0:
#             cnt1 += 1
#     if cnt1 == 2:
#         cnt2 += 1
#     cnt1 = 0
# print(cnt2)

# 소수 찾기 2
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중
# 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
# 이들 소수의 합은 620이고, 최솟값은 61이 된다.
from sys import stdin
M = int(stdin.readline())
N = int(stdin.readline())
cnt = 0
total = 0
demicallsit = list()
for i in range(M, N+1):
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        total += i
        demicallsit.append(i)
    cnt = 0

if total == 0:
    print(-1)
else:
    print(total)
    print(demicallsit[0])