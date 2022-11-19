import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

#######################################################################################
# d_row = [0, 0, 1, 1]
# d_col = [0, 1, 0, 1]

# order = -1


# def func(row, col, n):
#     global order
#     if n == 1:
#         for i in range(4):
#             order += 1
#             # print(row + d_row[i], col + d_col[i], order + i)
#             if row + d_row[i] == r and col + d_col[i] == c:
#                 print(order)
#                 sys.exit()
#     else:
#         func(row, col, n - 1)
#         func(row, col + 2 ** (n - 1), n - 1)
#         func(row + 2 ** (n - 1), col, n - 1)
#         func(row + 2 ** (n - 1), col + 2 ** (n - 1), n - 1)


# func(0, 0, N)
#######################################################################################
def solution(n, r, c):
    # print(n, r, c)
    if n == 0:
        return 0
    return 2 * (r % 2) + (c % 2) + 4 * solution(n - 1, r // 2, c // 2)


print(solution(N, r, c))

