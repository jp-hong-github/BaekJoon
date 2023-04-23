import sys
from collections import deque

input = sys.stdin.readline

# n,m 입력
n, m = map(int, input().split())
graph = []

start_point = None
# 그래프 입력
for row in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    # 시작점 찾기
    try:
        col = temp.index(2)
        start_point = (row, col)
    except:
        continue

q = deque([])
q.append(start_point)
distance = [[None for _ in range(m)] for _ in range(n)]
distance[start_point[0]][start_point[1]] = 0

direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

# bfs 구현
while q:
    row, col = q.popleft()
    # 상,하,좌,우 방향으로 이동
    for dRow, dCol in direction:
        nRow = row + dRow
        nCol = col + dCol
        # 그래프 안이면서 갈 수 있는 땅인 경우
        if 0 <= nRow < n and 0 <= nCol < m and graph[nRow][nCol] != 0:
            # 아직 가보지 않은 경우
            if distance[nRow][nCol] is None:
                distance[nRow][nCol] = distance[row][col] + 1
                q.append((nRow, nCol))
            # 이미 가 본 경우
            elif distance[nRow][nCol] is not None:
                # 최소 거리 갱신이 가능한 경우
                if distance[nRow][nCol] > distance[row][col] + 1:
                    distance[nRow][nCol] = distance[row][col] + 1
                    q.append((nRow, nCol))

# 그래프 출력
for row in range(n):
    for col in range(m):
        if col == m - 1:
            if graph[row][col] == 0:
                print(0)
            elif distance[row][col] is None:
                print(-1)
            else:
                print(distance[row][col])

        else:
            if graph[row][col] == 0:
                print(0, end=" ")
            elif distance[row][col] is None:
                print(-1, end=" ")
            else:
                print(distance[row][col], end=" ")
