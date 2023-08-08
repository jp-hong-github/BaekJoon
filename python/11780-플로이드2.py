n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]
before = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            before[a][b] = -1

for _ in range(m):
    a, b, cost = map(int, input().split())
    if graph[a][b] > cost:
        graph[a][b] = cost
    before[a][b] = a

path_result = []

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                before[a][b] = before[k][b]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j and before[i][j] != INF:
            temp = j
            res = [j]
            while temp != i:
                # print(i,j,"value :",before[i][temp])
                res.insert(0, before[i][temp])
                temp = before[i][temp]
            print(len(res), end=" ")
            for x in res:
                print(x, end=" ")
        else:
            print(0, end=" ")
        print()
