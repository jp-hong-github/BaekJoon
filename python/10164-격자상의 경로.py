import sys
import math

input = sys.stdin.readline

# dp 문제 였는데 그냥 수학으로 풀어버림
row, col, k = map(int, input().split())

if k == 0:
    print(math.comb(row - 1 + col - 1, col - 1))
else:
    if k % col == 0:
        circle_row = k // col
        circle_col = col
    else:
        circle_row = k // col + 1  # 2
        circle_col = k % col  # 3
    print(math.comb(circle_row - 1 + circle_col - 1, circle_col - 1) * math.comb(row - (circle_row) + (col - circle_col), (col - circle_col)))
