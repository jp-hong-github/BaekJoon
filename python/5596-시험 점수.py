import sys

input = sys.stdin.readline

m = list(map(int, input().split()))
n = list(map(int, input().split()))

if sum(m) >= sum(n):
    print(sum(m))
else:
    print(sum(n))
