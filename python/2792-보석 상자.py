import sys

input = sys.stdin.readline

n, m = map(int, input().split())
gem = [int(input()) for i in range(m)]

start = 1
end = max(gem)
result = float("inf")  # 결과-질투심

while start <= end:
    mid = (start + end) // 2

    count_get_gem = 0  # 보석을 갖게 된 아이의 수

    # 보석 나누기
    for g in gem:
        count_get_gem += g // mid
        if g % mid != 0:
            count_get_gem += 1

    if n > count_get_gem:  # 못 나누어준 아이가 있는 경우
        result = min(result, mid)
        end = mid - 1
    elif n == count_get_gem:  # 딱 알맞게 나누어준 경우
        result = min(result, mid)
        end = mid - 1
    else:  # 보석이 남은 경우
        start = mid + 1

print(result)
