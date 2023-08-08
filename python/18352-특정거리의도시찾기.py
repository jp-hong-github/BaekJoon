n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]

# 각각 -1 해야됨
# 그래프 생성
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

from collections import deque

result = [-1 for i in range(n + 1)]


def bfs(x):
    q = deque()
    q.append(x)
    result[x] = 0
    while q:
        temp = q.popleft()
        for i in graph[temp]:
            if result[i] == -1:
                result[i] = result[temp] + 1
                q.append(i)
    # result.sort()
    # 애초에 인덱 순으로 가져오니 sort하면 값에 따라 오름차순으로 정렬하므로 안됨
    # 테스트 케이스는 우연히 맞은거임


bfs(x)
t = 0
for u in range(1, n + 1):
    if k == result[u]:
        print(u)
        t = 1
if t == 0:
    print(-1)
# print(result)
