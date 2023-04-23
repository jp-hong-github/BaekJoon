import sys

input = sys.stdin.readline

graph = []
for _ in range(5):
    graph.append(list(map(str, input().split())))  # 일부로 str로 받음

# visited = []
# for _ in range(5):
#     visited.append([False for __ in range(5)])

dRow = [-1, 1, 0, 0]
dCol = [0, 0, -1, 1]

result = set()


def dfs(row, col, numStr, count):
    if count == 6:
        if numStr not in result:
            result.add(numStr)
    else:
        for i in range(4):
            nRow = dRow[i] + row
            nCol = dCol[i] + col
            if nRow >= 5 or nCol >= 5 or nRow < 0 or nCol < 0:
                continue
            # if visited[nRow][nCol] == True:
            #     continue
            numStr += graph[nRow][nCol]
            dfs(nRow, nCol, numStr, count + 1)
            numStr = numStr[:-1]


for i in range(5):
    for k in range(5):
        dfs(i, k, "", 0)
print(len(result))
# print(result)
