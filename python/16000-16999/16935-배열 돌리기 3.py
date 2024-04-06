import sys

input = sys.stdin.readline

row, col, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
operation = list(map(int, input().split()))


def operate(arr, op):
    row = len(arr)
    col = len(arr[0])
    temp_arr = [[0 for _ in range(col)] for _ in range(row)]

    # 상하 반전
    if op == 1:
        temp_arr = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                temp_arr[r][c] = arr[row - r - 1][c]

    # 좌우 반전
    elif op == 2:
        temp_arr = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                temp_arr[r][c] = arr[r][col - c - 1]

    # 오른쪽으로 90도 회전
    elif op == 3:
        temp_arr = [[0 for _ in range(row)] for _ in range(col)]
        for r in range(row):
            for c in range(col):
                temp_arr[c][row - 1 - r] = arr[r][c]

    # 왼쪽으로 90도 회전
    elif op == 4:
        temp_arr = [[0 for _ in range(row)] for _ in range(col)]
        for r in range(row):
            for c in range(col):
                temp_arr[col - 1 - c][r] = arr[r][c]

    # 왼쪽으로 90도 회전하는듯이 이동
    elif op == 5:
        for r in range(row // 2):
            # 1번 그룹 -> 2번 그룹
            for c in range(col // 2):
                temp_arr[r][c + col // 2] = arr[r][c]
            # 2번 그룹 -> 3번 그룹
            for c in range(col // 2, col):
                temp_arr[r + row // 2][c] = arr[r][c]

        for r in range(row // 2, row):
            # 3번 그룹 -> 4번 그룹
            for c in range(col // 2, col):
                temp_arr[r][c - col // 2] = arr[r][c]
            # 4번 그룹 -> 1번 그룹
            for c in range(col // 2):
                temp_arr[r - row // 2][c] = arr[r][c]

    # 오른쪽으로 90도 회전하듯이 이동
    elif op == 6:
        for r in range(row // 2):
            # 1번 그룹 -> 4번 그룹
            for c in range(col // 2):
                temp_arr[r + row // 2][c] = arr[r][c]
            # 2번 그룹 -> 1번 그룹
            for c in range(col // 2, col):
                temp_arr[r][c - col // 2] = arr[r][c]

        for r in range(row // 2, row):
            # 3번 그룹 -> 2번 그룹
            for c in range(col // 2, col):
                temp_arr[r - row // 2][c] = arr[r][c]
            # 4번 그룹 -> 3번 그룹
            for c in range(col // 2):
                temp_arr[r][c + col // 2] = arr[r][c]
    return temp_arr


for op in operation:
    arr = operate(arr, op)

for ar in arr:
    print(*ar)
