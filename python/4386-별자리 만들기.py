import sys

input = sys.stdin.readline


def cal_dist(star_1, star_2):
    return ((star_1[0] - star_2[0]) ** 2 + (star_1[1] - star_2[1]) ** 2) ** (0.5)


n = int(input())
graph = []
for _ in range(n):
    x, y = list(map(float, input().split()))
    graph.append([x, y])


if n == 1:
    print(0)
else:
    distance_list = []
    for star_1_idx in range(n - 1):
        for star_2_idx in range(star_1_idx + 1, n):
            distance_list.append(
                [cal_dist(graph[star_1_idx], graph[star_2_idx]), star_1_idx, star_2_idx]
            )

    distance_list.sort(key=lambda x: x[0])
    included_star_idx_list = set()
    result = 0
    edge_count = 0
    for selected_dist in distance_list:
        dist, star_1_idx, star_2_idx = selected_dist
        if (
            star_1_idx in included_star_idx_list
            and star_2_idx in included_star_idx_list
        ):
            pass
        else:
            print(
                "거리 : {}, 별의 좌표 : ({},{}), ({},{})".format(
                    round(dist, 3),
                    graph[star_1_idx][0],
                    graph[star_1_idx][1],
                    graph[star_2_idx][0],
                    graph[star_2_idx][1],
                )
            )
            included_star_idx_list.update([star_1_idx, star_2_idx])
            result += dist
            edge_count += 1
            if edge_count == n - 1:
                print(edge_count, n - 1)
                break

    print((included_star_idx_list))
    print(edge_count)
    print(result)
