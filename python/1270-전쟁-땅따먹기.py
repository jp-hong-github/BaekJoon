import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

for i in range(n):
    temp = list(map(int, input().split()))
    T_i, T_i_army_number = temp[0], temp[1:]
    max_army = Counter(T_i_army_number).most_common(1)

    if max_army[0][1] > T_i / 2:
        print(max_army[0][0])
    else:
        print("SYJKGW")
