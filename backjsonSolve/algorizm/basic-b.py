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
from sys import stdin
x = int(stdin.readline())
y = int(stdin.readline())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)