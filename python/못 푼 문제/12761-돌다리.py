import sys
from collections import deque

input = sys.stdin.readline
a, b, n, m = map(int, input().split())

q = deque([n])

# 각 지점으로 갈 수 있는 최소 거리
min_move = [0 for _ in range(100000)]

# bfs 코드
while q:
    current = q.popleft()
