import sys

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]

# 해당 칸에 value값이 들어가도 되는지 확인
def check(row, col, value):
    # 가로 확인
    if value in graph[row]:
        return False
    # 세로 확인
    for u in range(0, 9):
        if value == graph[u][col]:
            return False
    # 3x3 확인
    row_temp = []
    col_temp = []

    if 0 <= row and row < 3:
        row_temp = [0, 1, 2]
    elif 3 <= row and row < 6:
        row_temp = [3, 4, 5]
    else:
        row_temp = [6, 7, 8]

    if 0 <= col and col < 3:
        col_temp = [0, 1, 2]
    elif 3 <= col and col < 6:
        col_temp = [3, 4, 5]
    else:
        col_temp = [6, 7, 8]

    for cRow in row_temp:
        for cCol in col_temp:
            if value == graph[cRow][cCol]:
                return False
    # 모두 통과 시 True 반환
    return True


end = False


def sdk_00(row, col, count):
    global end
    # if row<=8 and col<=8:
    #     print('row:',row,' col:',col,' count:',count,' value:',graph[row][col])

    # 끝난 경우
    if count == 81 and end is False:
        # print('#######################################################')
        end = True
        for row in graph:
            for value in row:
                print(value, end=" ")
            print()
    elif end is True:
        return
    else:
        if graph[row][col] != 0:  # 이미 정해진 숫자가 있을 경우
            count += 1
            if col < 8:
                sdk_00(row, col + 1, count)
            elif col == 8 and row < 8:
                # print(' row:',row,' col:',col,' count:',count)
                sdk_00(row + 1, 0, count)
            else:
                sdk_00(row, col, count)
            count -= 1
        elif graph[row][col] == 0:  # 0인 경우
            for number in range(1, 10):
                if check(row, col, number):
                    graph[row][col] = number
                    count += 1
                    if col < 8:
                        sdk_00(row, col + 1, count)
                    elif col == 8 and row < 8:
                        sdk_00(row + 1, 0, count)
                    else:
                        sdk_00(row, col, count)
                    count -= 1
                    graph[row][col] = 0


sdk_00(0, 0, 0)

