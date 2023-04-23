import sys

input = sys.stdin.readline

n = int(input())

k = 0
move_list = []


def hanoi(n, start, middle, end):
    global k
    if n == 1:
        k += 1
        move_list.append((start, end))
    elif n >= 2:
        hanoi(n - 1, start, end, middle)
        k += 1
        move_list.append((start, end))
        hanoi(n - 1, middle, start, end)


hanoi(n, 1, 2, 3)
print(k)
for move in move_list:
    print(*move)
