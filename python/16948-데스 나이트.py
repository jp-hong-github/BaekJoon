import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

r1, c1, r2, c2 = map(int, input().split())


q = deque([(r1, c1, 0)])
visited = [[40001 for _ in range(n)] for _ in range(n)]
visited[r1][c1] = 0
destination = [(-2, -1), (-2, 1), (0, -2), (0, +2), (+2, -1), (+2, +1)]

while q:
    cr, cc, move_count = q.popleft()

    for dr, dc in destination:
        nr = cr + dr
        nc = cc + dc

        if not (0 <= nr < n and 0 <= nc < n):
            continue

        if visited[nr][nc] != 40001:
            if visited[nr][nc] <= move_count + 1:
                continue

        # print(nr, nc)
        visited[nr][nc] = move_count + 1
        q.append((nr, nc, move_count + 1))

if visited[r2][c2] == 40001:
    print(-1)
else:
    print(visited[r2][c2])
