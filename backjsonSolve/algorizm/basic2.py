# A + B (while문)
# while True:
#     try:
#         A, B = input().split()
#         A = int(A)
#         B = int(B)

#         if A <= 0 or B > 10:
#             break

#         Total = A + B
#         print(Total)

#     except:
#         break
# 더하기 싸이클
# n = input()
# num = n
# count = 0
# while True:
#     if len(num) == 1:
#         num = "0" + num
#     plus = str(int(num[0]) + int(num[1]))
#     num = num[-1] + plus[-1]
#     count += 1
#     if num == n:
#         print(count)
#         break
import sys

n = int(sys.stdin.readline())
num = n
count = 0

while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b * 10) + c

    count = count + 1
    if num == n:
        break

print(count)