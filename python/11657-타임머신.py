import sys
import math

input = sys.stdin.readline

INF = math.inf


def bellman_ford(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # 노드의 개수만큼 최단거리 테이블을 갱신
    for i in range(vertex_count):
        # 매 반복마다 모든 간선을 확인
        for j in range(edge_count):
            cur_node, next_node, weight = edges[j]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + weight:
                distance[next_node] = distance[cur_node] + weight
                # vertex_count번째 반복에서도 값이 갱신되나면 음수 순환이 존재
                if i == vertex_count - 1:
                    return True
    return False


# 노드의 개수 및 간선의 개수 입력
vertex_count, edge_count = map(int, input().split())
# 모든 간선에 대한 정보를 담을 리스트
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF for _ in range(vertex_count + 1)]

# 간선 정보 입력
for _ in range(edge_count):
    start, end, weight = map(int, input().split())
    # 가중치가 weight이며 start 노드에서 end 노드로 가는 간선
    edges.append((start, end, weight))

# 벨만 포드 알고리즘 수행
negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드까지의 최단 거리 출력
    for i in range(2, vertex_count + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
