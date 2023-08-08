import sys

input = sys.stdin.readline

t = int(input())


for i in range(t):
    n = int(input())
    new = []
    for k in range(n):
        new.append(list(map(int, input().split())))
    new.sort()
    count = 1
    dp = new[0][1]
    for u in range(1, n):
        if dp > new[u][1]:
            count += 1
            dp = new[u][1]
    print(count)
