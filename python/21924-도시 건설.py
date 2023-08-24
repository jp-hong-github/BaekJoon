import sys

input = sys.stdin.readline

N, M = map(int, input().split())

################################################################################
# 크루스칼 알고리즘

# graph = [list(map(int, input().split())) for _ in range(M)]

# parent = [i for i in range(N + 1)]


# def find(a):
#     if parent[a] != a:
#         parent[a] = find(parent[a])
#     return parent[a]


# def union(a, b):
#     r1 = find(a)
#     r2 = find(b)
#     if r1 != r2:
#         if r1 > r2:
#             parent[r1] = r2
#         else:
#             parent[r2] = r1


# def kruskal():
#     cost_sum = 0
#     mst = []

#     edges = sorted(graph, key=lambda x: x[2])

#     for edge in edges:
#         a, b, cost = edge

#         if find(a) == find(b):
#             continue

#         cost_sum += cost
#         mst.append(edge)
#         union(a, b)

#     if len(mst) == N - 1:  # 모든 건물을 연결할 수 있는 경우
#         return sum([i[2] for i in graph]) - cost_sum
#     else:  # 모든 건물을 연결할 수 없는 경우
#         return -1


# print(kruskal())

################################################################################
# 프림 알고리즘

import heapq

graph = [[] for _ in range(N + 1)]
total_all_cost = 0
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))
    total_all_cost += cost


def prim():
    heap = []
    visited = [False for _ in range(N + 1)]
    visited_count = 0
    cost_sum = 0

    for neighbor, cost in graph[1]:
        heapq.heappush(heap, (cost, 1, neighbor))

    visited[1] = True
    visited_count += 1

    while visited_count < N and heap:
        cost, current, neighbor = heapq.heappop(heap)

        if visited[neighbor]:
            continue

        cost_sum += cost
        visited[neighbor] = True
        visited_count += 1
        for next_neighbor, next_cost in graph[neighbor]:
            if not visited[next_neighbor]:
                heapq.heappush(heap, (next_cost, neighbor, next_neighbor))

    if visited_count == N:  # 모든 건물을 연결할 수 있는 경우
        return total_all_cost - cost_sum
    else:  # 모든 건물을 연결할 수 없는 경우
        return -1


print(prim())
