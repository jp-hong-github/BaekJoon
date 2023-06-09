import sys

input = sys.stdin.readline


def print_star():
    for idx, line in enumerate(result):
        for i, k in enumerate(line):
            if i == 0:
                continue
            print(f"{k}", end="")
            # print(f"{i}-{k}", end="")
        print()


def star(n, top_point, result):
    top_row = top_point[0]
    top_col = top_point[1]
    if n == 3:
        # 맨 위의 꼭짓점
        result[top_row][top_col] = "*"

        # 중간 부분
        result[top_row + 1][top_col - 1] = "*"
        result[top_row + 1][top_col + 1] = "*"

        # 맨 아래 부분
        for i in range(-2, 3, 1):
            result[top_row + 2][top_col + i] = "*"

    else:
        # 위의 삼각형
        star(n // 2, (top_row, top_col), result)

        # 왼쪽의 삼각형
        star(n // 2, (top_row + n // 2, top_col - n // 2), result)
        # 오른쪽의 삼각형
        star(n // 2, (top_row + n // 2, top_col + n // 2), result)


n = int(input())
result = [[" " for _ in range(n * 2)] for _ in range(n)]
star(n, (0, n), result)
print_star()

# n = 3
# cnt = 0
# while cnt <= 10:
#     result = [[" " for _ in range(n * 2)] for _ in range(n)]
#     star(n, (0, n), result)
#     print_star()
#     n *= 2
#     cnt += 1
