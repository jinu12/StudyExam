# 구구단
N = int(input())
for i in range(1, 10):
    print("{} * {} = {}".format(N, i, N * i))
# 두 정수 합구하기
T = int(input())
for i in range(1, T + 1, 1):
    A, B = input('').split()
    A = int(A)
    B = int(B)
    print("{} : ".format(i), A + B)
# 합 구하기
n = int(input())
total = 0
for i in range(n + 1):
    total = total + i
print(total)
# 빠른 두 정수 합구하기
import sys

T = int(sys.stdin.readline())
for i in range(1, T + 1, 1):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    print(A + B)
# N 찍기
N = int(input())
for i in range(1, N + 1):
    print(i)
# N 거꾸로 찍기
# import sys

N = int(sys.stdin.readline())
for i in range(N, 0, -1):
    print(i)
# 두 정수 합 테스트 케이스 추가
# import sys

T = int(sys.stdin.readline())
for i in range(1, T + 1, 1):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    print("Case #{}: {}".format(i, A + B))
# 두 정수 합 테스트 케이스 추가 입력값 추가
# import sys

T = int(sys.stdin.readline())
for i in range(1, T + 1, 1):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    print("Case #{}: {} + {} = {}".format(i, A, B, A + B))
# import sys

N = int(sys.stdin.readline())
for i in range(1, N + 1):
    print(" " * (N-i), end="")
    print("*" * i)
print("")

# import sys

N, X = sys.stdin.readline().split()
N = int(N)
X = int(X)
A = list(sys.stdin.readline().split())
for i in range(N):
    if int(A[i]) < X:
        print(A[i], end=' ')






