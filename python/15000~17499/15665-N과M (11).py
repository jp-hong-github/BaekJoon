import sys

input = sys.stdin.readline
n, m = map(int, input().split())
sys.setrecursionlimit(10000)

arr = list(map(int, input().split()))
arr.sort()

result = []
visited = [0] * n


def dfs(idx, count):
    if count == m:
        for u in result:
            print(u, end=" ")
        print()
    else:
        value = -1
        for i in range(0, n):
            if value != arr[i]:
                # print("i:",i,"idx+1:",idx+1,"n:",n,"count:",count)
                result.append(arr[i])
                value = arr[i]
                visited[i] = 1
                dfs(i, count + 1)
                result.pop()
                visited[i] = 0
    # print("Dfs")


dfs(-1, 0)

