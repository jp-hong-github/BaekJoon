import sys
from collections import defaultdict

input = sys.stdin.readline

# 데이터 입력
N, M = map(int, input().split())
K = int(input())
roads_under_construction = defaultdict(list)
for _ in range(K):
    a, b, c, d = map(int, input().split())
    # ! 가로, 세로를 잘 구별할 것
    if c == a + 1 or d == b + 1:
        roads_under_construction[(b, a)].append((d, c))
    else:
        roads_under_construction[(d, c)].append((b, a))


# 좌표가 그래프를 벗어나지 않았는지 확인하는 함수
def check_graph(r, c):
    if 0 <= r <= M and 0 <= c <= N:
        return True
    return False


# 현재 이동하고자 하는 길이 공사중인지 확인하는 함수
def check_construction(cr, cc, nr, nc):
    if (nr, nc) in roads_under_construction[(cr, cc)]:
        return True
    return False


# 현재 좌표가 방문할 수 있는지 확인하는 함수
def check_visited(r, c):
    if dp[r][c] != 0:
        return True
    return False


# DP 사용
dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
dp[0][0] = 1
for row in range(M + 1):
    for col in range(N + 1):
        if check_visited(row, col):
            if check_graph(row, col + 1) and not check_construction(row, col, row, col + 1):
                dp[row][col + 1] += dp[row][col]
            if check_graph(row + 1, col) and not check_construction(row, col, row + 1, col):
                dp[row + 1][col] += dp[row][col]

# for d in dp:
#     print(d)


print(dp[M][N])
