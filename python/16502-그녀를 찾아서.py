import sys

input = sys.stdin.readline

time = int(input())
M = int(input())
graph = {"A": {}, "B": {}, "C": {}, "D": {}}
graph_prob = {"A": 0.25, "B": 0.25, "C": 0.25, "D": 0.25}

for _ in range(M):
    start, end, prob = map(str, input().split())
    prob = float(prob)
    graph[start][end] = prob  # {"B":0.3}

for i in range(time):
    next_graph_prob = {"A": 0, "B": 0, "C": 0, "D": 0}
    for node in graph_prob:
        for move_node in graph[node]:
            next_graph_prob[move_node] += graph[node][move_node] * graph_prob[node]
    graph_prob = next_graph_prob
    # print(graph_prob)

for node in graph_prob:
    print(graph_prob[node] * 100)
