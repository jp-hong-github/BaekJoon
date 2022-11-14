import sys

input = sys.stdin.readline

n, m = map(int, input().split())

point = list(map(int, input().split()))
line = [list(map(int, input().split())) for _ in range(m)]

for start_point, end_point in line:
    result = 0
    # 처음으로 포함되는 인덱스와 마지막으로 포함되는 인덱스를 찾자
    first_point_idx = 0
    last_point_idx = 0
    #
    start_idx = 0
    end_idx = n - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if point[mid_idx] > start_point:
            end_idx = mid_idx - 1
        elif point[mid_idx] == start_point:
            first_point_idx = mid_idx
            break
        elif point[mid_idx] < start_point:
            start_idx = mid_idx + 1
    #
    start_idx = 0
    end_idx = n - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if point[mid_idx] > end_point:
            start_idx = mid_idx + 1
        elif point[mid_idx] == end_point:
            last_point_idx = mid_idx
            break
        elif point[mid_idx] < end_point:
            end_idx = mid_idx - 1

    #
    result = last_point_idx - first_point_idx + 1
    print(
        "result : %d,last point idx : %d, first point idx : %d, first_value : %d"
        % (result, last_point_idx, first_point_idx, point[first_point_idx])
    )
    print(result)
