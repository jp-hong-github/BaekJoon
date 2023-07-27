import sys

input = sys.stdin.readline

T = int(input())


def get_length(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)


for _ in range(T):
    point_list = []

    for _ in range(4):
        x, y = map(int, input().split())
        point_list.append((x, y))

    # 모든 길이의 리스트
    length_list = []
    for i in range(3):
        for k in range(i + 1, 4):
            length_list.append(get_length(point_list[i], point_list[k]))

    check = True  # 정사각형인지 확인
    length_list.sort()
    # 사각형의 변의 길이가 전부 같은지 확인
    # 만약 사각형이 정사각형일 경우 변의 길이보다 대각선의 길이가 길 것임
    for i in range(3):
        for k in range(i + 1, 4):
            if abs(length_list[i] - length_list[k]) > 0.00000000000001:
                check = False

    if not check:
        print(0)
        continue

    # 사각형의 대각선의 길이가 전부 같은지 확인
    if abs(length_list[4] - length_list[5]) > 0.00000000000001:
        print(0)
    else:
        print(1)
