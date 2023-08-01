import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
censors = list(map(int, input().split()))
censors.sort()

if N <= K:
    print(0)
else:
    dist = []
    for i in range(N - 1):
        dist.append(censors[i + 1] - censors[i])
    dist.sort()
    print(sum(dist[: len(dist) - (K - 1)]))
    # print(dist)
