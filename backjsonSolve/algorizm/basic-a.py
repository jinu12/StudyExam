# 나누기
from sys import stdin

print('나누기')

A, B = stdin.readline().split()
A, B = int(A), int(B)

print(A / B)

# 사칙 연산
# from sys import stdin
print('사칙 연산')

A, B = stdin.readline().split()
A, B = int(A), int(B)
print(A + B)
print(A - B)
print(A * B)
print(int(A / B))
print(A % B)

# 준하 놀람
# from sys import stdin
print('준하 놀람')

A = list(stdin.readline())
B = A + list('??!')
B.remove(B[len(A)-1])
for i in B:
    print(i, end='')


# 불기년도
print('불기년도')
# from sys import stdin

A = int(stdin.readline())
print(A-543)

# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# from sys import stdin
print('같은지 검증')

A, B, C = stdin.readline().split()
A, B, C = int(A), int(B), int(C)
print((A+B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# from sys import stdin
print('준하놀리기')
#
A = int(stdin.readline())
B = stdin.readline()
print("{}\n{}\n{}\n{}\n".format(A * int(B[2]), A * int(B[1]), A * int(B[0]), A * int(B)))
