from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())

# 그래프 입력
graph = []
for _ in range(r):
    graph.append((list(input().rstrip())))

dRow = [-1, 1, 0, 0]
dCol = [0, 0, -1, 1]

# bfs
def bfs(graph, row, col):
    q = deque([(row, col)])
    sheep = 0
    wolf = 0

    if graph[row][col] == "o":
        sheep += 1
    elif graph[row][col] == "v":
        wolf += 1

    graph[row][col] = "#"

    while q:
        cRow, cCol = q.popleft()

        for i in range(4):
            nRow = cRow + dRow[i]
            nCol = cCol + dCol[i]

            # 농장 공간을 볏어난 경우 무시
            if nRow < 0 or nCol < 0 or nRow >= r or nCol >= c:
                continue

            # 울타리이면 무시
            if graph[nRow][nCol] == "#":
                continue

            # 양인지 확인
            if graph[nRow][nCol] == "o":
                sheep += 1
            # 늑대인지 확인
            if graph[nRow][nCol] == "v":
                wolf += 1

            graph[nRow][nCol] = "#"
            q.append((nRow, nCol))

    # print("양 : %d, 늑대 : %d, row : %d, col : %d" % (sheep, wolf, row, col))
    if wolf >= sheep:
        return (0, wolf)
    else:
        return (sheep, 0)


# 계산
sheep_sum = 0
wolf_sum = 0
for row in range(r):
    for col in range(c):
        if graph[row][col] != "#":
            sheep, wolf = bfs(graph, row, col)
            sheep_sum += sheep
            wolf_sum += wolf

# 출력
print(sheep_sum, wolf_sum)
# for i in graph:
#     print(i)
