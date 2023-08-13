import sys
import heapq

input = sys.stdin.readline

V, E, P = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


# ==================================================================================================== #


# 첫 번째 방법 : 최단 경로에 건우가 있는지를 확인
def first():
    # ! 1번 정점에 건우가 있는 경우(출발 정점에 건우가 있는 경우)
    if P == 1:
        print("SAVE HIM")
        sys.exit()

    distance = [float("inf") for _ in range(V + 1)]
    distance[1] = 0

    h = []
    # 힙에는 (현재 정점,거리,건우가 있는 곳을 거쳤는지 확인)를 저장
    heapq.heappush(h, (1, 0, False))

    result = False

    while h:
        cur, dist, save = heapq.heappop(h)
        # print(cur, dist, save)

        if dist > distance[cur]:
            continue

        if cur == V and save:
            result = True

        for next, dist_to_next in graph[cur]:
            dist_sum = dist + dist_to_next
            # 값이 같은 경우는 생략하나 여기서는 건우를 구하는지 확인하기 위해
            # 값이 같은 경우에도 힙에 해당 정점을 삽입함
            if dist_sum <= distance[next]:
                save_him_check = save
                # 건우가 있는 정점인 경우
                if next == P:
                    save_him_check = True

                distance[next] = dist_sum
                heapq.heappush(h, (next, dist_sum, save_him_check))

    if result:
        print("SAVE HIM")
    else:
        print("GOOD BYE")


# ==================================================================================================== #


# 두 번째 방법 : 1번 정점->건우까지의 거리 + 건우->V번 정점까지의 거리 == 1번 정점->V번 정점까지의 거리인 경우 건우를 구할 수 있음
def second():
    def dijkstra(start_v):
        distance = [float("inf") for _ in range(V + 1)]
        distance[start_v] = 0

        h = []
        # 힙에는 (현재 정점,거리)를 저장
        heapq.heappush(h, (start_v, 0))

        while h:
            cur, dist = heapq.heappop(h)

            if dist > distance[cur]:
                continue

            for next, dist_to_next in graph[cur]:
                dist_sum = dist + dist_to_next
                # 값이 같은 경우는 생략하나 여기서는 건우를 구하는지 확인하기 위해
                # 값이 같은 경우에도 힙에 해당 정점을 삽입함
                if dist_sum <= distance[next]:
                    distance[next] = dist_sum
                    heapq.heappush(h, (next, dist_sum))
        return distance

    vertex_1_distance = dijkstra(1)
    vertex_P_distance = dijkstra(P)

    if vertex_1_distance[V] == vertex_1_distance[P] + vertex_P_distance[V]:
        print("SAVE HIM")
    else:
        print("GOOD BYE")


# ==================================================================================================== #


second()
