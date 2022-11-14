import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N, K = map(int, input().split())

    start = 0
    end = 10000

    num = 0
    result = 0
    while start <= end:
        mid = (start + end) // 2
        temp = (N - 1) - K * (mid + 1) * mid // 2
        if temp > 0:
            start = mid + 1
            num = mid
            result = temp
        elif temp == 0:
            num = mid
            result = temp
            break
        else:
            end = mid - 1
    if result == 0:
        if num % 2 == 0:
            print("%d R")
