# cSpell:ignore HaruHaru

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for __ in range(N)]

q = deque([(0, 0)])
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

flag = False
while q:
    row, col = q.popleft()

    if row < 0 or col < 0 or row >= N or col >= N:
        continue
    if visited[row][col] == True:
        continue
    if graph[row][col] == -1:
        flag = True
        break

    visited[row][col] = True
    for i in range(4):
        nr = row + dr[i] * graph[row][col]
        nc = col + dc[i] * graph[row][col]
        q.append((nr, nc))

if flag is False:
    print("Hing")
else:
    print("HaruHaru")
