import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    start = 1
    end = N
    result = 0
    while start <= end:
        # mid의 값이 건넌 돌의 개수
        mid = (start + end) // 2
        # 등차수열의 합 공식을 사용하여 건너는 거리를 구함
        # 점프하는 거리가 1, 2, ... , mid 이므로 mid * (mid + 1) // 2
        # 마지막 점프의 거리는 조절할 수 있으므로 상관없음
        if mid * (mid + 1) // 2 > N:
            end = mid - 1
        else:
            start = mid + 1
            result = mid
    print(result)
