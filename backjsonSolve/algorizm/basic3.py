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
from sys import stdin
count = 0
numlist = list()
x = list()
y = list()
for i in range(10):
    numlist.append(int(stdin.readline()))
print(numlist)
for i in numlist:
    x.append(i % 42)
print(x)
for i in range(len(x)):
    for j in range(len(x)):
        if x[i] == x[j]:
            count = count + 1
            if count == 2:
                print(x[i])
                y.append(x[i])
    count = 0
print(len(x)-len(y))


