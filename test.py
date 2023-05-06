import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    graph.append([int(i) for i in input().rstrip()])


# 각 연결된 영역이 연결된 칸의 개수
area_count_dict = defaultdict(int)

# 벽이 없는 곳에서의 영역의 칸의 개수 세기(검색해보니 플러드 필 알고리즘이라고 한다.)
visited = [[False for _ in range(m)] for _ in range(n)]

# 0은 일반 칸, 1은 벽이므로 2부터 넘버링 시작
area_number = 2
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for row in range(n):
    for col in range(m):
        if graph[row][col] == 0 and visited[row][col] is False:
            q = deque([(row, col)])
            area_count = 0

            while q:
                cRow, cCol = q.popleft()
                visited[cRow][cCol] = True
                graph[cRow][cCol] = area_number
                area_count += 1

                for dRow, dCol in direction:
                    nRow = cRow + dRow
                    nCol = cCol + dCol

                    if not (0 <= nRow < n and 0 <= nCol < m):
                        continue

                    if graph[nRow][nCol] == 0 and visited[nRow][nCol] is False:
                        q.append((nRow, nCol))

            area_count_dict[area_number] = area_count
            area_number += 1

# 벽 없애는 경우 계산
for row in range(n):
    for col in range(m):
        if graph[row][col] == 1:
            result = 1
            neighbor_numbering_set = set()
            for dRow, dCol in direction:
                nRow = row + dRow
                nCol = col + dCol
                if not (0 <= nRow < n and 0 <= nCol < m):
                    continue

                if graph[nRow][nCol] != 1:
                    neighbor_numbering_set.add(graph[nRow][nCol])

            for i in list(neighbor_numbering_set):
                result += area_count_dict[i]

            print(result, end="")
        else:
            print(0, end="")
    print()
