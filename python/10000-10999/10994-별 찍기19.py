n = int(input())

star = [[" " for _ in range(4 * n - 3)] for __ in range((4 * n - 3) * 2 + 1)]


def stars(n, row, col):
    if n == 1:
        star[row][col] = "*"
        return

    l = 4 * n - 3
    for z in range(l):
        star[row][col + z] = "*"  # 위
        star[row + 2 * z][col] = "*"  # 왼쪽
        star[row + 2 * l - 2][col + z] = "*"  # 아래
        star[row + 2 * z][col + l - 1] = "*"  # 오른쪽

    stars(n - 1, row + 4, col + 2)


stars(n, 0, 0)

q = 0
for line in star:
    if q % 2 == 0:
        for point in line:
            print(point, end="")
        print()
    q += 1
