import sys, math
from collections import deque

NEGATIVE_INF = -math.inf
input = sys.stdin.readline

N, start_city, end_city, M = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]  # 각 간선을 지날 때 드는 비용
earn = list(map(int, input().split()))  # 각 도시에서 버는 돈
dist = [NEGATIVE_INF for _ in range(N + 1)]

# 도착지점이 사이클과 연결되어 있는지 확인
def end_city_in_cycle(node):
    visited = [False for _ in range(N)]
    q = deque([])
    q.append(node)
    while q:
        cur_node = q.popleft()
        visited[cur_node] = True

        if cur_node == end_city:
            return True
        else:
            for edge in edges:
                if edge[0] == cur_node and visited[edge[1]] == False:
                    visited[edge[1]] = True
                    q.append(edge[1])
    return False


def bf(start_city):
    dist[start_city] = earn[start_city]
    cycle_check = False
    # end_city_in_cycle = False
    for i in range(N):
        for k in range(M):
            cur_node, next_node, cost = edges[k]
            if dist[cur_node] != NEGATIVE_INF and dist[next_node] < dist[cur_node] - cost + earn[next_node]:
                dist[next_node] = dist[cur_node] - cost + earn[next_node]
                if i == N - 1:
                    # cycle_check = True
                    if end_city_in_cycle(next_node):
                        return True
                    # if next_node == end_city:
                    # end_city_in_cycle = True

    # 이렇게 풀면 안되는 듯
    # 건너건너 갱신되는게 있는 경우가 존재하는 듯
    # if cycle_check and end_city_in_cycle:  # 싸이클(순환)이 존재하는가 만약 존재한다면 도착지가 포함되는가
    # return True

    return False


cycle_check = bf(start_city)


if dist[end_city] == NEGATIVE_INF:
    print("gg")
elif cycle_check:
    print("Gee")
else:
    print(dist[end_city])

