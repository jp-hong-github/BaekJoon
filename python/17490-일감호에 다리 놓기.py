import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())


num_of_stones_required_each_building = [0] + list(map(int, input().split()))

roads_under_construction = []  # 공사중인 길의 리스트
for _ in range(m):
    roads_under_construction.append(list(map(int, input().split())))
roads_under_construction.sort()

# 공사가 1개이 이하인 경우 돌다리 놓을 필요도 없이 모든 강의동을 갈 수 있음
if m <= 1:
    print("YES")


else:
    # 연결된 강의실끼리 중 와우도를 연결하는 최소의 돌의 개수
    num_of_stones_required_each_connected_building = []

    # 공사중인 길의 첫번째 강의실
    first_building_in_construction_road = 1
    for idx, construction_paths in enumerate(roads_under_construction):
        # n번째 강의실과 1번 강의실 사이의 길이 연결되어 있는 경우
        if idx == m - 1 and construction_paths[0] != n:
            # 기존의 1번 강의실이 연결된 그룹에서의 최소 돌의 개수와 n번째와 연결되 강의실들끼리의 최소 돌의 개수를 비교
            if construction_paths[1] == n:
                num_of_stones_required_each_connected_building[0] = min(
                    num_of_stones_required_each_connected_building[0], num_of_stones_required_each_building[construction_paths[1]]
                )
            else:
                num_of_stones_required_each_connected_building[0] = min(
                    num_of_stones_required_each_connected_building[0], min(num_of_stones_required_each_building[construction_paths[1] :])
                )

        num_of_stones_required_each_connected_building.append(
            min(num_of_stones_required_each_building[first_building_in_construction_road : construction_paths[0] + 1])
        )

        first_building_in_construction_road = construction_paths[1]

    if sum(num_of_stones_required_each_connected_building) <= k:
        print("YES")
    else:
        print("NO")
