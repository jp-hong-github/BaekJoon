import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
K = int(input())

# 행을 켤 수 있는 조건을 만족하는 행
row_list = []

# 행을 켤 수 있는지 확인
for row in range(N):
    zero_count = graph[row].count(0)
    if zero_count <= K and zero_count % 2 == K % 2:
        row_list.append(row)

row_dict = defaultdict(int)
# 행을 켤 수 있는 행끼리 같은 것이 있는지 비교 및 확인
for row in row_list:
    row_dict[tuple(graph[row])] += 1


if row_dict:
    print(max(row_dict.values()))
else:
    print(0)
