from sys import stdin
A, B = stdin.readline().split()
A, B = int(A), int(B)
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
