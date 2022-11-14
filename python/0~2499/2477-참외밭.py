import sys

input = sys.stdin.readline


K = int(input())
point = []
for _ in range(6):
    point.append(list(map(int, input().split())))

# 4 -> 2 -> 3 -> 1
# [1,3] [3,2] [2,4] [4,1]

check = [[1, 3], [3, 2], [2, 4], [4, 1]]
w = 0
h = 0
for i in range(6):
    for case in check:
        if point[i][0] == case[0] and point[(i + 1) % 6][0] == case[1]:
            area_minus = point[i][1] * point[(i + 1) % 6][1]

    if point[i][0] == 3 or point[i][0] == 4:
        h = max(h, point[i][1])
    else:
        w = max(w, point[i][1])

print((h * w - area_minus) * K)
