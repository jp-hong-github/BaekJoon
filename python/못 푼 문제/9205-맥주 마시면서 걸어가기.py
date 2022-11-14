from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    house = list(map(int, input().split()))
    store = []
    for __ in range(n):
        store.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))

    q = deque([])
    q.append((house[0], house[1], 20))  # 현재 x 좌표, 현재 y 좌표, 남은 맥주의 수

