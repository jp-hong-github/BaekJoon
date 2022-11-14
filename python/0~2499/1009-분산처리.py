import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    result = a % 10
    for i in range(b - 1):
        result = (result % 10) * (a % 10)
    if result == 0:
        print(10)
    else:
        print(result % 10)
