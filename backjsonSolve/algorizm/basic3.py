# 최솟값 최대값 구하기

# import sys
#
# N = int(sys.stdin.readline())
# numlist = list()
# numlists = sys.stdin.readline().split()
# for i in range(len(numlists)):
#     numlist.append(int(numlists[i]))
# print(min(numlist), end=' ')
# print(max(numlist))

# 최대값과 인덱스
# import sys
# numlist = []
# count = 0
# maxs = 0
# for i in range(1, 10):
#     numlist.append(int(sys.stdin.readline()))
# print(max(numlist))
# print(numlist.index(max(numlist)) + 1)

# 숫자의 개수
# A = int(input())
# B = int(input())
# C = int(input())
# Total = A * B * C
# Totallist = sorted([int(a) for a in str(Total)])
# for i in range(len(Totallist)):
#     if i < len(Totallist) - 1:
#         if Totallist[i] == Totallist[i+1]:
#             pass
#         else:
#             print(Totallist[i])
#             print(Totallist.count(Totallist[i]))

# count = 0
# A = int(input())
# B = int(input())
# C = int(input())
# Total = A * B * C
# Totallist = sorted([int(a) for a in str(Total)])
#
# for i in range(10):
#     for j in Totallist:
#         if i == j:
#             count += 1
#     print(count)
#     count = 0
# from sys import stdin
# count = 0
# numlist = list()
# x = list()
# y = list()
# for i in range(10):
#     numlist.append(int(stdin.readline()))
# print(numlist)
# for i in numlist:
#     x.append(i % 42)
# print(x)
# for i in range(len(x)):
#     for j in range(len(x)):
#         if x[i] == x[j]:
#             count = count + 1
#             if count == 2:
#                 print(x[i])
#                 y.append(x[i])
#     count = 0
# print(len(x)-len(y))

# 평균
"""
세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.
"""

# from sys import stdin
#
# C = list()
# N = int(stdin.readline())
# total = 0
# B = stdin.readline().split()
# for i in range(N):
#     C.append(int(B[i]))
# for i in C:
#     total += i
# print(total / len(C) / max(C) * 100)


# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# from sys import stdin
# X = list()
# N = int(stdin.readline())
# OX = list()
# for i in range(N):
#     X.append(stdin.readline().split())
# for i in X:
#     OX.append(i)
# print(len(X[0]))
# for i in range(len(X[0])):
#     print(str(X[0][i]), end='  ')

# 평균은 넘겠지
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

from sys import stdin
X = list()
N = list()
CN = list()
total = 0
count = 0
C = int(stdin.readline())
for i in range(C):
    X.append(stdin.readline().split())
    N.append(int(X[i][0]))
    del X[i][0]
for i in range(len(X)):
    for j in range(len(X[i])):
        total += int(X[i][j])
    for j in range(len(X[i])):
        if total / N[i] < int(X[i][j]):
            count = count + 1
    print("%.3f" % (count / N[i] * 100) + "%")
    count = 0
    total = 0


# for i in range(len)
