import sys
from collections import deque

input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

current_truck_idx = 0
current_weight_sum = 0
total_truck_bridge = 0
result_time = 0

bridge = deque()

while True:
    if bridge and bridge[0][1] == result_time:
        current_weight_sum -= bridge[0][0]
        total_truck_bridge -= 1
        bridge.popleft()

    if current_truck_idx < n:
        current_truck_weight = trucks[current_truck_idx]
        if (
            total_truck_bridge + 1 <= w
            and current_truck_weight + current_weight_sum <= l
        ):
            bridge.append([current_truck_weight, result_time + w])
            total_truck_bridge += 1
            current_weight_sum += current_truck_weight
            current_truck_idx += 1

    result_time += 1

    if not bridge and current_truck_idx >= n:
        break

print(result_time)
