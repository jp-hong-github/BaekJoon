import heapq
from decimal import Decimal


def prim(graph, start_vertex, num_of_vertex):
    # 방문한 정점을 저장하는 집합
    visited = set()

    # 최소 스패닝 트리의 간선들을 저장하는 리스트
    minimum_spanning_tree = []

    # 시작 정점을 방문한 것으로 표시
    visited.add(start_vertex)

    # 시작 정점과 연결된 간선들을 우선순위 큐에 추가
    edges = []
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(edges, (weight, start_vertex, neighbor))

    # 모든 정점을 방문할 때까지 반복
    while len(visited) < num_of_vertex:
        # 가장 가중치가 작은 간선을 선택
        weight, u, v = heapq.heappop(edges)

        # 이미 방문한 정점이면 무시
        if v in visited:
            continue

        # 새로운 정점을 방문한 것으로 표시
        visited.add(v)

        # 최소 스패닝 트리에 간선 추가
        minimum_spanning_tree.append((u, v, weight))

        # 새로운 정점과 연결된 간선들을 우선순위 큐에 추가
        for neighbor, weight in graph[v]:
            heapq.heappush(edges, (weight, v, neighbor))

    return minimum_spanning_tree


n = int(input())

stars = []
for _ in range(n):
    x, y = list(map(str, input().split()))
    x = Decimal(x)
    y = Decimal(y)
    stars.append((x, y))

graph = [[] for _ in range(n)]
for i in range(n):
    for k in range(n):
        if i == k:
            continue
        distance = (
            (stars[i][0] - stars[k][0]) ** Decimal("2")
            + (stars[i][1] - stars[k][1]) ** Decimal("2")
        ) ** Decimal("0.5")
        graph[i].append((k, distance))

mst = prim(graph, 0, n)
print(sum(i[2] for i in mst))
