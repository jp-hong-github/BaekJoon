import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

