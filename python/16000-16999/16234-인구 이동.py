import sys
from collections import deque

input = sys.stdin.readline

n, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# bfs를 사용하여 연합 서치
def find_county_union(r, c, visited):
    total_people = graph[r][c]
    total_country = 1
    visited[r][c] = True
    union_set = set([(r, c)])

    q = deque([(r, c)])
    while q:
        cr, cc = q.popleft()
        for dRow, dCol in direction:
            nr = cr + dRow
            nc = cc + dCol

            if not (0 <= nr < n and 0 <= nc < n):
                continue

            if visited[nr][nc]:
                continue

            if not (L <= abs(graph[cr][cc] - graph[nr][nc]) <= R):
                continue

            visited[nr][nc] = True
            union_set.add((nr, nc))
            total_country += 1
            total_people += graph[nr][nc]
            q.append((nr, nc))

    if total_country == 1:
        return False
    else:
        people_in_one_county = int(total_people / total_country)
        for ur, uc in list(union_set):
            graph[ur][uc] = people_in_one_county
        return True


result = 0
while True:
    check = False  # 인구 이동이 생겼는지 확인하는 변수
    visited = [[False for _ in range(n)] for _ in range(n)]
    for rr in range(n):
        for cc in range(n):
            if not visited[rr][cc]:
                temp = find_county_union(rr, cc, visited)
                if temp:
                    check = True

    if check:
        result += 1
        check = False
    else:
        break

print(result)
