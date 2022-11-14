#
# ! 한글 번역이 이상하므로 질문 검색에 있는 원문 번역을 참조할 것
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

money = []
for _ in range(N):
    money.append(int(input()))

start = max(money)  # 최소한의 k의 값
end = sum(money)
result = end
while start <= end:
    mid = (start + end) // 2  # 임시의 k
    current = 0  # 현재 금액 합
    count = 0

    # all_list = []  # 나눈 모든 집합
    # temp = []  # 임시
    for i in range(N):
        current += money[i]
        if current > mid:
            count += 1
            current = money[i]

    if current > 0:
        count += 1

    if count > M:
        start = mid + 1
    else:
        if mid < result:
            result = mid
        end = mid - 1

print(result)
