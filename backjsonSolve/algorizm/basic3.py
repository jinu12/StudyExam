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

from sys import stdin

C = list()
N = int(stdin.readline())
total = 0
B = stdin.readline().split()
for i in range(N):
    C.append(int(B[i]))
for i in C:
    total += i
print(total / len(C) / max(C) * 100)

