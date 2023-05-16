import sys
import math
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())

counter = Counter()
start_height = math.inf
end_height = 0
for _ in range(n):
    temp_list = list(map(int, input().split()))
    start_height = min(start_height, min(temp_list))
    end_height = max(end_height, max(temp_list))
    counter.update(temp_list)


result_time = math.inf
result_height = -1

for height in range(start_height, end_height + 1):
    total_block = b
    total_time = 0
    for current_height, height_count in counter.items():
        if current_height > height:
            block_count = current_height - height
            total_block += block_count * height_count
            total_time += 2 * block_count * height_count
        elif current_height == height:
            continue
        else:
            block_count = height - current_height
            total_block -= block_count * height_count
            total_time += block_count * height_count

    # print(height, total_block, total_time)
    if total_block >= 0:
        if result_time > total_time:
            result_time = total_time
            result_height = height
        elif result_time == total_time:
            result_height = max(result_height, height)
    else:
        break

print(result_time, result_height)

# ! 이분 탐색으로 풀면 에러
# while start_height <= end_height:
#     mid_height = (start_height + end_height) // 2
#     total_block = b
#     total_time = 0
#     for row in range(n):
#         for col in range(m):
#             if graph[row][col] > mid_height:
#                 block_count = graph[row][col] - mid_height
#                 total_block += block_count
#                 total_time += 2 * block_count
#             elif graph[row][col] == mid_height:
#                 continue
#             else:
#                 block_count = mid_height - graph[row][col]
#                 total_block -= block_count
#                 total_time += block_count

#     print(mid_height, total_block, total_time)
#     if total_block >= 0:
#         if result_time > total_time:
#             result_time = total_time
#             result_height = mid_height
#         elif result_time == total_time:
#             result_height = max(result_height, mid_height)
#         start_height = mid_height + 1
#     else:
#         end_height = mid_height - 1
