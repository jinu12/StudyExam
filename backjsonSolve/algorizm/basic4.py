# 재귀
from sys import stdin
N = int(stdin.readline())


def factorial(num):
    total = 1
    for i in range(1, num + 1):
        total = total * i
    return total


print(factorial(N))

