import sys

input = sys.stdin.readline
n, m = map(int, input().split())
sys.setrecursionlimit(10000)
arr = list(map(int, input().split()))
arr.insert(0, 0)
arr.sort()


result = []


def dfs(idx, count):
    if count == m:
        for i in result:
            print(i, end=" ")
        print()
    else:
        value = -1
        for i in range(0, n + 1):
            if i >= idx and arr[i] != 0 and value != arr[i]:  #
                value = arr[i]
                result.append(arr[i])
                dfs(i, count + 1)
                result.pop()


dfs(0, 0)
