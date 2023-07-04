import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

numbers = [0] + [int(input()) for _ in range(n)]
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[numbers[i]].append(i)

visited = [False for _ in range(n + 1)]
result = []


def dfs(cur, cycle):
    visited[cur] = True
    cycle.append(cur)

    for next in graph[cur]:
        if next not in cycle:
            dfs(next, cycle[:])
        else:
            result.extend(cycle)
            return


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, [])

print(len(result))
for i in sorted(result):
    print(i)
