import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())
    result = 0
    for x in range(n, m + 1, 1):
        if x == 0:
            result += 1
            continue
        while x > 0:
            if x % 10 == 0:
                result += 1
            x //= 10
    print(result)
