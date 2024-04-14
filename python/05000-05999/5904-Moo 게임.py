import sys

input = sys.stdin.readline


def solution(n):
    value = 3
    idx = 1
    while True:
        if value >= n:
            break
        idx += 1
        value = value + idx + 2 + value

    for i in range(idx, -1, -1):
        half = (value - (i + 2)) // 2

        if n <= half:
            value = half
        elif n > half + i + 2:
            value = half
            n -= half + i + 2
        else:
            if n == half + 1:
                print("m")
                return
            else:
                print("o")
                return

    if n == 1:
        print("m")
    elif n == 2 or n == 3:
        print("o")


n = int(input())
solution(n)
