# 20210119 복습

m, n = map(int, input().split())
snack = list(map(int, input().split()))

snack.sort()

start = 1
end = snack[-1]

result = 0

# 이진탐색
while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in range(0, n):
        count += snack[i] // mid

    if count >= m:
        result = mid
        # result에 mid 값으로 초기화된다면 어쨋든 최적해는 아니더라도 조카들에게 나눠줄 수 있다는 것을 의미
        start = mid + 1
    else:
        end = mid - 1

print(result)
"""
0이 나오는 경우는 
4 3
1 1 1

같이 애초에 막대 과자의 길이의 합이 n보다 작은 경우이다.
n 이상이면 길이를 1로 나누어서라도 줄 수 있기 때문이다.
"""
