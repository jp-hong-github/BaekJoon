import sys

input = sys.stdin.readline

sys.setrecursionlimit(int(10e3))
tree = []


while True:
    try:
        tree.append(int(input()))
    except:
        break


def rec(num, value):
    if num > value:
        return
    temp = value + 1
    for i in range(num + 1, value + 1):
        if tree[num] < tree[i]:
            temp = i
            break
    rec(num + 1, temp - 1)
    rec(temp, value)
    print(tree[num])


rec(0, len(tree) - 1)
