# 재귀
# 팩토리얼
# from sys import stdin
# N = int(stdin.readline())
#
#
# def factorial(num):
#     total = 1
#     for i in range(1, num + 1):
#         total = total * i
#     return total
#
#
# print(factorial(N))

# 파보나치 수열
from sys import stdin
N = int(stdin.readline())
fabo = list()


def fabonachi(num):
    global fabo
    for i in range(0, num+1):
        if i == 0:
            fabo.append(0)
        elif i <= 2:
            fabo.append(1)
        else:
            fabo.append(fabo[i-1] + fabo[i-2])
    return fabo[num]


print(fabonachi(N))


# test = list(int(i) for i in range(3))
# print(test)
# test.append(test[2] + test[1])
# print(test)
# for i in range(10):
#     if i == 0:
#         test.append(1)
#     if i == 1:
#         test.append(2)
#     else:
#         sum(test[i-1],test[i-2]
# print(test)