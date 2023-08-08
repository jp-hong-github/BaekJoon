import sys

input = sys.stdin.readline
sys.setrecursionlimit(15000)

n = int(input())
danji = []

for i in range(n):
    danji.append(list(map(int, input().rstrip())))


def dfs(x, y):
    total = 1
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return 0
    if danji[y][x] == 1:
        danji[y][x] = 0
        total += dfs(x - 1, y)
        total += dfs(x, y - 1)
        total += dfs(x + 1, y)
        total += dfs(x, y + 1)
        return total
    return 0


result = []
for i in range(n):
    for j in range(n):
        num = dfs(i, j)
        if num != 0:
            result.append(num)

print(len(result))
result.sort()
for u in result:
    print(u)
