import sys

input = sys.stdin.readline


n = int(input())
result = [[" " for _ in range(n)] for _ in range(n)]


def star(n, left_top_point, result):
    left_x = left_top_point[0]
    left_y = left_top_point[1]
    if n == 3:
        result[left_y][left_x] = "*"
        result[left_y][left_x + 1] = "*"
        result[left_y][left_x + 2] = "*"

        result[left_y + 1][left_x] = "*"
        result[left_y + 1][left_x + 2] = "*"

        result[left_y + 2][left_x] = "*"
        result[left_y + 2][left_x + 1] = "*"
        result[left_y + 2][left_x + 2] = "*"

    else:
        # 상단
        for i in range(3):
            star(n // 3, (left_x + i * (n // 3), left_y), result)
        # 중간
        star(n // 3, (left_x, left_y + (n // 3)), result)
        star(n // 3, (left_x + 2 * (n // 3), left_y + (n // 3)), result)
        # 하단
        for i in range(3):
            star(n // 3, (left_x + i * (n // 3), left_y + 2 * (n // 3)), result)


star(n, (0, 0), result)

for line in result:
    for s in line:
        print(s, end="")
    print()
