import sys

input = sys.stdin.readline

############################################################################
# 크루스칼 알고리즘을 사용

# N = int(input())
# graph = []
# for i in range(N):
#     temp = list(map(int, input().split()))
#     for k in range(N):
#         if i == k:
#             continue
#         else:
#             graph.append((i, k, temp[k]))
# parent = [i for i in range(N + 1)]


# def find(v, parent):
#     if parent[v] != v:
#         parent[v] = find(parent[v], parent)
#     return parent[v]


# def union(v1, v2, parent):
#     r1 = find(v1, parent)
#     r2 = find(v2, parent)
#     if r1 != r2:
#         if r1 > r2:
#             parent[r1] = r2
#         else:
#             parent[r2] = r1


# def kruskal(graph, parent):
#     edges = sorted(graph, key=lambda x: x[2])

#     mst = []

#     for edge in edges:
#         v1, v2, _ = edge

#         if find(v1, parent) != find(v2, parent):
#             mst.append(edge)
#             union(v1, v2, parent)

#     return mst


# mst = kruskal(graph, parent)
# print(sum([i[2] for i in mst]))

############################################################################
# 프림 알고리즘을 사용

import heapq

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def prim(graph, start):
    visited = set()
    mst = []

    visited.add(start)

    edges = []
    for neighbor in range(N):
        if start == neighbor:
            continue
        else:
            heapq.heappush(edges, (graph[start][neighbor], start, neighbor))

    while len(visited) < N:
        weight, already_vertex_mst, candidate_vertex_mst = heapq.heappop(edges)

        if candidate_vertex_mst in visited:
            continue

        visited.add(candidate_vertex_mst)

        mst.append((already_vertex_mst, candidate_vertex_mst, weight))

        for neighbor in range(N):
            if candidate_vertex_mst == neighbor:
                continue
            else:
                heapq.heappush(edges, (graph[candidate_vertex_mst][neighbor], candidate_vertex_mst, neighbor))

    return mst


mst = prim(graph, 0)
print(sum([i[2] for i in mst]))
