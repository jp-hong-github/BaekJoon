import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cube = [[0 for _ in range(m + 2)]]
for _ in range(n):
    temp = list(map(int, input().split()))
    temp.append(0)
    temp.insert(0, 0)
    cube.append(temp)
cube.append([0 for _ in range(m + 2)])

dRow = [0, 0, -1, 1]
dCol = [-1, 1, 0, 0]
result = 0

for row in range(1, n + 1):
    for col in range(1, m + 1):
        current_h = cube[row][col]
        result_case = 0
        for i in range(4):
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if (0 <= nRow and nRow <= n + 1) and (0 <= nCol and nCol <= m + 1):
                temp_h = cube[nRow][nCol]
                height_difference = current_h - temp_h
                if height_difference > 0:
                    result_case += height_difference
        result += result_case

result += 2 * n * m
print(result)
