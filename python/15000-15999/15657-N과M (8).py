import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

result = []


def dfs(idx, count):
    if count == m:
        for i in result:
            print(i, end=" ")
        print()
    else:
        for i in range(idx, n):
            result.append(arr[i])
            dfs(i, count + 1)
            result.pop()


dfs(0, 0)
