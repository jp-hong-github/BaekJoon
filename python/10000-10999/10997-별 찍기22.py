n = int(input())


def star(arr, n, row, col):
    if n == 1:
        arr[row][col] = "*"
        arr[row + 1][col] = "*"
        arr[row + 2][col] = "*"

        return

    col += 1
    # print('up')
    for _ in range(5 + 4 * (n - 2)):
        col -= 1
        # print(row,col)
        arr[row][col] = "*"

    # print('left')
    # row-=1
    for _ in range(6 + 4 * (n - 2)):
        row += 1
        # print(row,col)
        arr[row][col] = "*"

    # print('down')
    # col-=1
    for _ in range(4 + 4 * (n - 2)):
        col += 1
        # print(row,col)
        arr[row][col] = "*"
    # print('up')

    # row+=1
    for _ in range(4 + 4 * (n - 2)):
        row -= 1
        # print(row,col)
        arr[row][col] = "*"

    col -= 1
    # print(row,col)
    arr[row][col] = "*"
    star(arr, n - 1, row, col - 1)


if n == 1:
    print("*")

else:
    number = 4 * n
    arr = [[" " for _ in range(1 + 4 * (n - 1))] for __ in range(number - 1)]
    star(arr, n, 0, 4 * (n - 1))
    q = 1
    for line in arr:
        if q == 2:
            print("*")
        else:
            for point in line:
                print(point, end="")
            print()
        q += 1
