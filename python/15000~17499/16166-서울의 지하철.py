import sys

input = sys.stdin.readline

N = int(input())

graph = {}

for i in range(N):
    temp = list(map(int, input().split()))
    graph[i] = temp[1:]

destination = int(input())

from collections import deque

#############
# print()
# for i in graph:
#     print(graph[i])
# print()
#############

q = deque([(0, 0)])  # 역 번호, 환승 횟수
result = sys.maxsize
while q:
    current_station, transfer_num = q.popleft()
    # print(current_station, transfer_num)
    if current_station == destination:
        if transfer_num < result:
            result = transfer_num
        continue

    temp_line_key_to_del = []
    for line_key in graph:
        if current_station in graph[line_key]:
            graph[line_key].remove(current_station)
            for station in graph[line_key]:
                if current_station == 0:
                    q.append((station, transfer_num))
                else:
                    q.append((station, transfer_num + 1))
            temp_line_key_to_del.append(line_key)

    for line_key_to_del in temp_line_key_to_del:
        del graph[line_key_to_del]

if result == sys.maxsize:
    print(-1)
else:
    print(result)
