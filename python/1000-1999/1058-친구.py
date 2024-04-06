import sys

input = sys.stdin.readline

n = int(input())
INF = int(10e9)
graph = []

# 그래프 입력
for _ in range(n):
    temp = list(input().rstrip())
    temp_changed = []
    for char in temp:
        if char == "N":
            temp_changed.append(INF)
        else:
            temp_changed.append(1)
    graph.append(temp_changed)

# 플로이드 와샬 알고리즘
for i in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# 대각선을 다시 무한으로 초기화(자기 자신은 제외해야 하기 때문이다)
for i in range(n):
    graph[i][i] = INF

# 결과 계산
result = 0
for i in range(n):
    result = max(result, graph[i].count(1) + graph[i].count(2))

print(result)
