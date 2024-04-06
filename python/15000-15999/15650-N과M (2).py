import sys

input = sys.stdin.readline
n, m = map(int, input().split())

import itertools

data = [i for i in range(1, n + 1)]

comb = list(itertools.combinations(data, m))
for case in comb:
    for u in case:
        print(u, end=" ")
    print()
