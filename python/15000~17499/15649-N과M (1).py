import sys

input = sys.stdin.readline
n, m = map(int, input().split())
sys.setrecursionlimit(10000)

arr = [i for i in range(1, n + 1)]

result = []
visited = [0] * n


def dfs(idx, count):
    if count == m:
        for u in result:
            print(u, end=" ")
        print()
    else:
        for i in range(0, n):
            if i != idx and visited[i] == 0:
                # print("i:",i,"idx+1:",idx+1,"n:",n,"count:",count)
                result.append(arr[i])
                visited[i] = 1
                dfs(i, count + 1)
                result.pop()
                visited[i] = 0
    # print("Dfs")


dfs(-1, 0)

