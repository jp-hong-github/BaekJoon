import sys

input = sys.stdin.readline

r, c = map(int, input().split())

string = []

for i in range(r):
    string.append(list(map(str, input().rstrip())))

result = 0
dRow = [-1, 1, 0, 0]
dCol = [0, 0, -1, 1]


def dfs(row, col, soneString):
    global result
    over = True
    for i in range(4):
        cRow = dRow[i] + row
        cCol = dCol[i] + col
        if cRow < 0 or cCol < 0 or cRow >= r or cCol >= c:
            continue
        if string[cRow][cCol] in soneString:
            continue
        soneString = soneString + string[cRow][cCol]
        dfs(cRow, cCol, soneString)
        soneString = soneString[:-1]

        over = False
    if over is True:
        result = max(result, len(soneString))


dfs(0, 0, string[0][0])
print(result)
