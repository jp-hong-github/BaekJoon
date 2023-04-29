import sys
import copy

input = sys.stdin.readline

N = int(input())

board = [list(input().rstrip()) for _ in range(N)]

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# row행 col열의 사탕을 d방향에 있는 사탕과 바꾼 후 확인
def test_board(row, col, d):
    board_temp = copy.deepcopy(board)

    if not (0 <= row + d[0] < N and 0 <= col + d[1] < N):
        return 0

    # 바꾸고자 하는 사탕의 색깔이 같은 경우
    if board_temp[row][col] == board_temp[row + d[0]][col + d[1]]:
        return 0

    result = 0

    # 사탕 교환
    temp = board_temp[row + d[0]][col + d[1]]
    board_temp[row + d[0]][col + d[1]] = board_temp[row][col]
    board_temp[row][col] = temp

    # 최대 길이 확인
    for rr in range(N):
        current_color = ""
        temp_result_r = 1
        for cc in range(N):
            if current_color == board_temp[rr][cc]:
                temp_result_r += 1
                result = max(result, temp_result_r)
            else:
                current_color = board_temp[rr][cc]
                result = max(result, temp_result_r)
                temp_result_r = 1

    for cc in range(N):
        current_color = ""
        temp_result_c = 1
        for rr in range(N):
            if current_color == board_temp[rr][cc]:
                temp_result_c += 1
                result = max(result, temp_result_c)
            else:
                current_color = board_temp[rr][cc]
                result = max(result, temp_result_c)
                temp_result_c = 1
    result = max(result, temp_result_c)

    return result


answer = 0
for row in range(N):
    for col in range(N):
        for d in direction:
            answer = max(answer, test_board(row, col, d))

print(answer)
