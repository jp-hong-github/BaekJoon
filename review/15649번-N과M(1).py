import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def backtracking(value, count, arr):
    if count == m:
        print(*arr)
        return
    else:
        for i in range(1, n + 1):
            if i != value and i not in arr:
                arr.append(i)
                backtracking(i, count + 1, arr)
                arr.pop()
        return


for i in range(1, n + 1):
    arr = [i]
    backtracking(i, 1, arr)
