import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())

graph = []
for _ in range(R):
    temp = list(map(str, input().rstrip()))
    graph.append(temp)

result = 0
visited = [[False for _ in range(C)] for __ in range(R)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def backtracking(row, col, count):
    # 조건문 : 도착점 확인 후 결과값 증가
    global result
    if row == 0 and col == C - 1:
        if count == K:
            result += 1
        return
    else:  # 조건문 : 도착점이 아니므로 이미 지나가지 않은 지점 중 지나가기
        for idx in range(4):
            next_row = row + directions[idx][0]
            next_col = col + directions[idx][1]
            if (0 <= next_row <= R - 1) and (0 <= next_col <= C - 1):  # 다음 지점이 범위 내인지 확인
                if graph[next_row][next_col] != "T":
                    if visited[next_row][next_col] is False:  # 이미 지나간 점인지 확인
                        visited[next_row][next_col] = True
                        backtracking(next_row, next_col, count + 1)
                        visited[next_row][next_col] = False


visited[R - 1][0] = True
backtracking(R - 1, 0, 1)
print(result)

