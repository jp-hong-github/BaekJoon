import sys

input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

result = {-1: 0, 0: 0, 1: 0}


def solution(row, col, length, matrix):
    count_minus_one = 0
    count_zero = 0
    count_one = 0

    first_value = matrix[row][col]
    break_flag = False
    for row_ in range(row, row + length):
        for col_ in range(col, col + length):
            if matrix[row_][col_] == first_value:
                pass
            else:
                break_flag = True
                break
        if break_flag:
            break

    if break_flag is False:
        if first_value == -1:
            count_minus_one += 1
        elif first_value == 0:
            count_zero += 1
        else:
            count_one += 1
    else:
        for in_row in range(row, row + length, length // 3):
            for in_col in range(col, col + length, length // 3):
                count_minus_one_, count_zero_, count_one_ = solution(
                    in_row, in_col, length // 3, matrix
                )
                count_minus_one += count_minus_one_
                count_zero += count_zero_
                count_one += count_one_

    return (count_minus_one, count_zero, count_one)


for result in solution(0, 0, N, matrix):
    print(result)
