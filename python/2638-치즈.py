import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dRow = [-1, 1, 0, 0]
dCol = [0, 0, -1, 1]

result_time = 0
# 1. 빈 공간 찾기
# 2. 치즈 없애기

from collections import deque

air_num = -1
while True:
    isCheeseLive = False
    q = deque([(0, 0)])

    while q:
        cRow, cCol = q.popleft()
        if graph[cRow][cCol] <= 0 and graph[cRow][cCol] != air_num:
            graph[cRow][cCol] = air_num
            for i in range(4):
                nRow = dRow[i] + cRow
                nCol = dCol[i] + cCol

                if nRow < 0 or nCol < 0 or nRow >= n or nCol >= m:
                    continue
                else:
                    q.append((nRow, nCol))

    # 빈 공간 찾음, air_num이 공기의 번호 , 치즈 없애는 부분

    # for i in graph:
    #     for k in i:
    #         print("%2d"%(k),end = ' ')
    #     print()
    # print()
    # if result_time==10:
    #     break

    for row in range(n):
        for col in range(m):
            if graph[row][col] == 1:
                isCheeseLive = True
                air_count = 0
                for i in range(4):
                    nRow = dRow[i] + row
                    nCol = dCol[i] + col
                    if graph[nRow][nCol] < 0:
                        air_count += 1
                if air_count >= 2:
                    graph[row][col] = 0

    if isCheeseLive is False:
        break
    else:
        result_time += 1
    air_num -= 1


print(result_time)
