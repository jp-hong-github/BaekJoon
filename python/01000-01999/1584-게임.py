import sys
from collections import deque

input = sys.stdin.readline


graph = [[0 for _ in range(501)] for __ in range(501)]

N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            graph[x][y] = 1


M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            graph[x][y] = 2


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 다익스트라 포기
# 가중치가 0인 간선이 존재하는데 이로 인해 빙글빙글 돌게 됨
# 어떻게 처리해야 할 지 모르겠음

# q = []
# heapq.heappush(q, ((0, 0), 0))

# while q:
#     now_pos, cur_life = heapq.heappop(q)
#     for idx in range(4):
#         nx = now_pos[0] + dx[idx]
#         ny = now_pos[1] + dy[idx]
#         # print(nx, ny)
#         if 0 <= nx <= 500 and 0 <= ny <= 500:
#             if graph[nx][ny] == "death":
#                 continue
#             elif graph[nx][ny] == "danger":
#                 next_life = cur_life + 1
#             else:
#                 next_life = cur_life

#             if minus_life[nx][ny] < next_life:
#                 continue
#             else:
#                 minus_life[nx][ny] = next_life
#                 heapq.heappush(q,((nx,ny),next_life))

visited = [[False for _ in range(501)] for __ in range(501)]
q = deque()
q.append((0, 0, 0))
visited[0][0] = True
can_reach = False

while q:
    x, y, life = q.popleft()
    if x == 500 and y == 500:
        can_reach = True
        print(life)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= 500 and 0 <= ny <= 500 and not visited[nx][ny]:
            if graph[nx][ny] == 0:
                q.appendleft((nx, ny, life))
                visited[nx][ny] = True
            elif graph[nx][ny] == 1:
                q.append((nx, ny, life + 1))
                visited[nx][ny] = True

if not can_reach:
    print(-1)
