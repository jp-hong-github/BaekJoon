import sys
import math

input = sys.stdin.readline
# INF = math.inf
INF = 10001


# def dfs(node, edges, visited):
#     visited[node] = True
#     for a, b, c in edges:
#         if a == node and not visited[b]:
#             dfs(b, edges, visited)


def bellman_ford(start, distance, vertex_count, edges):

    distance[start] = 0
    for i in range(vertex_count):
        for j in range(len(edges)):
            cur_node, next_node, cost = edges[j]
            if  distance[next_node] > distance[cur_node] + cost:
                distance[next_node] = distance[cur_node] + cost
                if i == vertex_count - 1:
                    # // # dfs를 통해 음수 간선 순환에 시작점이 있는지 확인해주어야 함
                    # visited = [False for _ in range(vertex_count + 1)]
                    # dfs(next_node, edges, visited)
                    # if visited[1]:
                    return True
    return False


t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())

    edges = []
    for _ in range(m):
        A, B, cost = map(int, input().split())
        edges.append((A, B, cost))
        edges.append((B, A, cost))
    for _ in range(w):
        starting, arrival, minus_cost = map(int, input().split())
        edges.append((starting, arrival, -minus_cost))

    distance = [INF for _ in range(n + 1)]

    negative_cycle = bellman_ford(1, distance, n, edges)
    if negative_cycle:
        print("YES")
    else:
        print("NO")

