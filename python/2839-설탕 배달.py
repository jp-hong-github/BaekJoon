import sys

input = sys.stdin.readline

n = int(input())
k = n // 5
while k >= 0:
    if n == 5 * k + 3 * (((n - 5 * k) // 3)):
        print(k + (((n - 5 * k) // 3)))
        break
    k -= 1

if k < 0:
    print(-1)

