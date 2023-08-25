import sys

input = sys.stdin.readline

N, M = map(int, input().split())
s, e = map(int, input().split())
#############################################################################
# & 크루스칼 알고리즘

# & 크루스칼 알고리즘을 사용할 때 s의 루트와 e의 루트가 같으면 됨

# graph = [list(map(int, input().split())) for _ in range(M)]
# parent = [i for i in range(N + 1)]


# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]


# def union(x, y):
#     rx = find(x)
#     ry = find(y)
#     if rx < ry:
#         parent[ry] = rx
#     else:
#         parent[rx] = ry


# def kruskal():
#     result = float("inf")
#     edges = sorted(graph, key=lambda x: -x[2])

#     # 간선의 비용이 가장 큰 것부터 연결함
#     for a, b, weight in edges:
#         if find(a) != find(b):
#             union(a, b)
#             # 간선의 비용이 가장 큰 것부터 연결하므로 예외가 없음
#             result = min(result, weight)
#         # 시작 지점과 종료 지점의 루트가 같은 경우
#         # 서로 연결되었음을 의미
#         if find(s) == find(e):
#             return result
#     return 0


# print(kruskal())


#############################################################################
# & 프림 알고리즘
# & 이 문제는 프림 알고리즘이 더 적합

import heapq

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def prim(s, e):
    result = float("inf")
    visited = set()
    visited_e = False
    h = []
    for s_neighbor, w in graph[s]:
        # 최대 힙을 위해 w의 음수를 저장함을 주의
        heapq.heappush(h, (-w, s, s_neighbor))

    visited.add(s)

    while not visited_e and h:
        w, cur, neighbor = heapq.heappop(h)
        w = -w

        if neighbor in visited:
            continue

        result = min(result, w)

        visited.add(neighbor)
        if neighbor == e:
            visited_e = True
            continue

        for next, next_w in graph[neighbor]:
            if next not in visited:
                heapq.heappush(h, (-next_w, neighbor, next))

    if visited_e:
        return result
    else:
        return 0


print(prim(s, e))
