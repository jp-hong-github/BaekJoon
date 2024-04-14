import sys

input = sys.stdin.readline

s = int(input())

sum = 0
n = 0
i = 1
while sum <= s:
    sum += i
    n += 1
    i += 1

print(n - 1)
