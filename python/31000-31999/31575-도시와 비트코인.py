import sys
from collections import deque

input = sys.stdin.readline

result = "No"

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

q = deque([(0, 0)])

while q:
    r, c = q.popleft()

    if r == M - 1 and c == N - 1:
        result = "Yes"
        break

    # 오른쪽 또는 아래쪽으로만 이동 가능
    for dr, dc in [(0, 1), (1, 0)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < M and 0 <= nc < N and graph[nr][nc] == 1:
            q.append((nr, nc))
            graph[nr][nc] = 0

print(result)
