import sys

input = sys.stdin.readline

t = int(input())

for case in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    data.insert(0, 0)  # 1 ~ n
