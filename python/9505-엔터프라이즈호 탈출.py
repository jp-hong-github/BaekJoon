import sys
import heapq

input = sys.stdin.readline

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T = int(input())
for _ in range(T):
    K, W, H = map(int, input().split())

    # 클링온 전투선의 클래스 입력
    classes_of_klingon_combat_ship = {}
    for _ in range(K):
        class_name, time = map(str, input().split())
        classes_of_klingon_combat_ship[class_name] = int(time)

    # 그래프 입력
    graph = []
    start_pos = None
    for i in range(H):
        row = list(input().rstrip())
        graph.append(row)
        if start_pos is None:
            for k in range(W):
                if row[k] == "E":
                    start_pos = (i, k)  # 초기 엔터프라이즈호의 위치를 저장

    time_to_move = [[float("inf") for _ in range(W)] for _ in range(H)]  # 해당 지점까지 이동하는 데 걸린 시간
    heap = [(0, start_pos[0], start_pos[1])]  # (걸린 시간,현재 위치)를 저장
    time_to_move[start_pos[0]][start_pos[1]] = 0

    # 데이크스트라 알고리즘을 사용
    # result = float("inf")
    while heap:
        current_time, cRow, cCol = heapq.heappop(heap)

        # 탈출이 가능한 경우
        if cRow == 0 or cRow == H - 1 or cCol == 0 or cCol == W - 1:
            print(current_time)
            break
            # ! 최솟값을 하나만 찾으면 됨
            # result = min(result, current_time)
            # continue

        for dRow, dCol in direction:
            nRow = cRow + dRow
            nCol = cCol + dCol

            # 사각형의 범위를 벗어난 경우
            if not (0 <= nRow < H and 0 <= nCol < W):
                continue

            # 시작 지점인 경우
            if graph[nRow][nCol] == "E":
                continue

            # 시간이 더 걸리는 경우
            next_time = current_time + classes_of_klingon_combat_ship[graph[nRow][nCol]]
            if time_to_move[nRow][nCol] <= next_time:
                continue

            time_to_move[nRow][nCol] = next_time
            heapq.heappush(heap, (next_time, nRow, nCol))

    # print(result)
