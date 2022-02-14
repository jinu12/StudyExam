# 비교문제
# from sys import stdin
# A, B = stdin.readline().split()
# A, B = int(A), int(B)
# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# else:
#     print("==")
# 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램
# from sys import stdin
# score = int(stdin.readline())
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")
# 사분면 고르기
# from sys import stdin
# x = int(stdin.readline())
# y = int(stdin.readline())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)
# 45분 일찍
# from sys import stdin
# H, M = stdin.readline().split()
# H, M = int(H), int(M)
# if M < 45:
#     if H == 0:
#         H = 23
#         M = (M + 60) - 45
#     else:
#         H = H - 1
#         M = (M + 60) - 45
# else:
#     M = M - 45
# print("{} {}".format(H, M))
# 오븐 시계
# from sys import stdin
# H, M = stdin.readline().split()
# H, M = int(H), int(M)
# C = int(stdin.readline())
# if M + C >= 60:
#     H = H + (M+C) // 60
#     M = (M+C) % 60
#     if H >= 24:
#         H = H - 24
# else:
#     M += C
# print("{} {}".format(H, M))

# 주사위 세 개
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
from sys import stdin
A, B, C = stdin.readline().split()
A, B, C = int(A), int(B), int(C)
numlist = [A, B, C]
if A == B == C:
    print(10000 + 1000 * A)
elif A == B != C or A == C != B:
    print(1000 + 100 * A)
elif B == C != A or B == A != C:
    print(1000 + 100 * B)
else:
    print(max(numlist) * 100)
