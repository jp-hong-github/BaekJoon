import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


q = deque()
q.append([1, 0])  # 현재 위치, 거리
result = {"num": 1, "dist": 0, "same": None}
visited = [False for _ in range(N + 1)]
visited[1] = True
while q:
    current, dist = q.popleft()
    for next in graph[current]:
        if visited[next] is not True:
            visited[next] = True

            # 거리가 같은 경우
            if dist + 1 == result["dist"]:
                if next < result["num"]:
                    result["num"] = next
                result["same"] += 1

            # 거리가 먼 경우
            elif dist + 1 > result["dist"]:
                result = {"num": next, "dist": dist + 1, "same": 1}
            # print(result)
            q.append([next, dist + 1])

print("%d %d %d" % (result["num"], result["dist"], result["same"]))

