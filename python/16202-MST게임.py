import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = deque([])
for i in range(1, m + 1):
    a, b = map(int, input().split())
    graph.append((a, b, i))


# 각 노드의 조상을 찾음
def find(v, parent):
    if parent[v] != v:
        parent[v] = find(parent[v], parent)
    return parent[v]


# 조상 노드를 더 작은 값을 가진 조상 노드로 합침
def union(v1, v2, parent):
    root1 = find(v1, parent)
    root2 = find(v2, parent)
    if root1 != root2:
        if root1 > root2:
            parent[root2] = root1
        else:
            parent[root2] = root1


def kruskal(graph, parent):
    # graph = sorted(graph, key=lambda x: x[2])

    minimum_spanning_tree = []

    for edge in graph:
        v1, v2, weight = edge

        # 사이클이 형성되지 않는 경우
        if find(v1, parent) != find(v2, parent):
            minimum_spanning_tree.append(edge)
            union(v1, v2, parent)

    return minimum_spanning_tree


result = []
for j in range(k):
    parent = [i for i in range(n + 1)]
    mst = kruskal(graph, parent)
    if len(mst) == n - 1:
        result.append(sum([i[2] for i in mst]))
    else:
        for l in range(k - j):
            result.append(0)
        break
    graph.popleft()

print(*result)
