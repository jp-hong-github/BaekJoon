import sys

input = sys.stdin.readline

A, B = map(int, input().split())

if A == B:
    for _ in range(A):
        print(1, end="")
else:
    for _ in range(abs(A - B)):
        print(1, end="")

