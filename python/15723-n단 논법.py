n = int(input())

INF = int(1e9)

graph = [[INF] * (26 + 1) for _ in range(26 + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] == 0

for i in range(n):
    string = input()

    start, end = string[0], string[-1]
    # print(start,end)
    # print(ord(start),ord(end))
    graph[ord(start) - 96][ord(end) - 96] = 1

for k in range(1, 26 + 1):
    for a in range(1, 26 + 1):
        for b in range(1, 26 + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


m = int(input())

for i in range(m):
    string = input()
    start, end = string[0], string[-1]
    if graph[ord(start) - 96][ord(end) - 96] != INF:
        print("T")
    else:
        print("F")
