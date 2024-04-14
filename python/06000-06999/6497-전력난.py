import sys
import heapq

input = sys.stdin.readline


def find_root(v, parents):
    if v != parents[v]:
        parents[v] = find_root(parents[v], parents)
    return parents[v]


def union(v1, v2, parents):
    root1 = find_root(v1, parents)
    root2 = find_root(v2, parents)
    if root1 != root2:
        if root1 > root2:
            parents[root1] = root2
        else:
            parents[root2] = root1


while True:
    house, road = list(map(int, input().split()))
    if house == 0 and road == 0:
        break

    parents = [i for i in range(house)]
    graph = []
    original_total_money = 0  # 기존의 전기료의 합계
    for _ in range(road):
        x, y, z = list(map(int, input().split()))
        original_total_money += z
        heapq.heappush(graph, (z, x, y))

    light_roads = []  # 불을 킨 도로들
    only_light_money = 0  # 불을 킨 도로의 전기료의 합
    while len(light_roads) < house - 1:
        cost, x, y = heapq.heappop(graph)

        if find_root(x, parents) != find_root(y, parents):
            only_light_money += cost
            light_roads.append((cost, x, y))
            union(x, y, parents)

    # print(light_roads)
    print(original_total_money - only_light_money)
