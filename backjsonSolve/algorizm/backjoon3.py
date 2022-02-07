# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수
num = int(input(""))
b = []
for j in range(1, num + 1):
    b.append(j)


def solve(a: list):
    ans = 0
    for i in a:
        ans += i
    return ans


print(solve(b))