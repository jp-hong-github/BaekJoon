import sys
from math import gcd

input = sys.stdin.readline


def solve():
    d1, d2 = map(int, input().split())
    arr = [[0] * d2 for _ in range(d2)]
    cnt = 0
    for r in range(d1, d2 + 1):
        for i in range(1, r + 1):
            c = gcd(i, r)
            a, b = i // c, r // c
            if not arr[a - 1][b - 1]:
                arr[a - 1][b - 1] = 1
                cnt += 1
    print(cnt)


solve()
