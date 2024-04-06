import sys
from collections import deque

input = sys.stdin.readline

result = []

while 1:
    # 건물 입력 받기
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    building = []
    start_point = None
    end_point = None
    for i in range(l):
        floor = []
        for j in range(r):
            temp = list(input().rstrip())
            if "S" in temp:
                start_point = (i, j, temp.index("S"))
            elif "E" in temp:
                end_point = (i, j, temp.index("E"))
            floor.append(temp)

        building.append(floor)
        input()

    # print(start_point, end_point)
    # bfs 수행
    q = deque([start_point])

    visited = [[[float("inf") for _ in range(c)] for _ in range(r)] for _ in range(l)]
    visited[start_point[0]][start_point[1]][start_point[2]] = 0
    direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while q:
        cl, cr, cc = q.popleft()

        for dl, dr, dc in direction:
            nl, nr, nc = cl + dl, cr + dr, cc + dc

            if not ((0 <= nl < l) and (0 <= nr < r) and (0 <= nc < c)):
                continue

            if building[nl][nr][nc] == "#":
                continue

            if visited[nl][nr][nc] != float("inf"):
                continue

            q.append((nl, nr, nc))
            visited[nl][nr][nc] = visited[cl][cr][cc] + 1

    if visited[end_point[0]][end_point[1]][end_point[2]] != float("inf"):
        result.append(
            f"Escaped in {visited[end_point[0]][end_point[1]][end_point[2]]} minute(s)."
        )
    else:
        result.append("Trapped!")

for r in result:
    print(r)
