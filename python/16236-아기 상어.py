import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    if 9 in temp:
        current_shark_position = (i, temp.index(9), 0)  # row, col,크기,이동횟수
    graph.append(temp)

# 초기 상어의 크기 : 2
# 2마리 먹으면 2->3
# 3마리 먹으면 3->4
# 4마리 먹으면 4->5
# 5마리 먹으면 5->6
# 6마리 먹으면 6->7

# 1.엄마 상어를 부르는 조건(끝나는 조건)
# 2.먹을 수 있는 먹이
# 3.먹을 수 있는 먹이 중 가장 가까운 것(위쪽 왼쪽)
# 4.이동 후 상어의 크기 증가 판별

result_time = 0
eat_count = 0
flag = True
current_shark_size = 2

while flag:
    q = deque([current_shark_position])
    fish_candidate = {"row": N, "col": N, "move_count": N ** 2 + 1}
    visited = [[False for _ in range(N)] for _ in range(N)]

    visited[current_shark_position[0]][current_shark_position[1]] = True

    while q:
        row, col, move_count = q.popleft()
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_row = row + d_row
            n_col = col + d_col
            if 0 <= n_row <= N - 1 and 0 <= n_col <= N - 1 and visited[n_row][n_col] == False:
                if graph[n_row][n_col] == 0 or graph[n_row][n_col] == 9:  # 단순 길
                    q.append((n_row, n_col, move_count + 1))

                elif graph[n_row][n_col] > current_shark_size:  # 크기가 더 큰 물고기
                    continue

                elif graph[n_row][n_col] == current_shark_size:  # 크기가 같은 물고기
                    q.append((n_row, n_col, move_count + 1))

                elif graph[n_row][n_col] < current_shark_size:  # 크기가 작은 물고기
                    if move_count + 1 <= fish_candidate["move_count"]:
                        if fish_candidate["row"] > n_row:
                            fish_candidate = {"row": n_row, "col": n_col, "move_count": move_count + 1}
                        elif fish_candidate["row"] == n_row and fish_candidate["col"] > n_col:
                            fish_candidate = {"row": n_row, "col": n_col, "move_count": move_count + 1}

                visited[n_row][n_col] = True

    if fish_candidate["row"] == N and fish_candidate["col"] == N:
        break
    else:
        result_time += fish_candidate["move_count"]

        # 현재 상어 위치 갱신
        graph[current_shark_position[0]][current_shark_position[1]] = 0
        current_shark_position = (fish_candidate["row"], fish_candidate["col"], 0)
        graph[fish_candidate["row"]][fish_candidate["col"]] = 9
        #######################
        # print(fish_candidate)
        # for i in graph:
        #     print(i)
        # print("=" * 100)
        #######################
        eat_count += 1
        # 현재 상어 크기 갱신
        if current_shark_size == eat_count:
            current_shark_size += 1
            eat_count = 0

print(result_time)
