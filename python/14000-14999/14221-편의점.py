import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a].append((c, b))
    graph[b].append((c, a))


p, q = list(map(int, input().split()))
candidate_house_list = list(map(int, input().split()))  # 집의 후보지
candidate_store_list = list(map(int, input().split()))  # 편의점의 후보지


# 각 편의점마다 다익스트라 알고리즘 실행 <- 시간 초과 발생
# for store in candidate_store_list:

# ! 처음 부터 힙에 모든 편의점을 넣음
dist_list = [float("inf") for _ in range(n + 1)]
heap = []
# 모든 편의점의 거리는 0으로 설정
for store in candidate_store_list:
    dist_list[store] = 0
    heappush(heap, (0, store))


while heap:
    current_dist, current_pos = heappop(heap)
    if current_dist > dist_list[current_pos]:
        continue

    for neighbor_dist, neighbor in graph[current_pos]:
        total_dist = current_dist + neighbor_dist

        if total_dist < dist_list[neighbor]:
            dist_list[neighbor] = total_dist
            heappush(heap, (total_dist, neighbor))


# 정점 중 집까지의 거리만 계산
min_dist_result = float("inf")
answer_house = 0
for candidate in candidate_house_list:
    if min_dist_result > dist_list[candidate] or (
        min_dist_result == dist_list[candidate] and answer_house > candidate
    ):
        min_dist_result = dist_list[candidate]
        answer_house = candidate

print(answer_house)
