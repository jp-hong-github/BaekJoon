import sys

input = sys.stdin.readline
N, M = list(map(int, input().split()))
point = list(map(int, input().split()))
point.sort()
line = [list(map(int, input().split())) for _ in range(M)]

result = []

for line_start, line_end in line:

    smallest_num_include = -1
    biggest_num_include = -1

    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if line_start <= point[mid]:
            smallest_num_include = mid
            end = mid - 1
        else:
            start = mid + 1

    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if point[mid] <= line_end:
            biggest_num_include = mid
            start = mid + 1
        else:
            end = mid - 1

    result.append((smallest_num_include, biggest_num_include))

for r in result:
    if r[1] != -1 and r[0] != -1 and r[1] >= r[0]:
        print(r[1] - r[0] + 1)
    else:
        print(0)
