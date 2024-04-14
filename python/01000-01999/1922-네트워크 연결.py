import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))


def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union(parents, a, b):
    a_root = find_parent(parents, a)
    b_root = find_parent(parents, b)
    if a_root > b_root:
        parents[a_root] = b_root
    else:
        parents[b_root] = a_root


def kruskal(graph, parents):
    edges = sorted(graph, key=lambda x: x[2])

    mst = []
    for edge in edges:
        v1, v2, weight = edge

        if find_parent(parents, v1) != find_parent(parents, v2):
            mst.append(edge)
            union(parents, v1, v2)

    return mst


mst = kruskal(graph, [i for i in range(n + 1)])
# print(mst)
# print()
print(sum([i[2] for i in mst]))
