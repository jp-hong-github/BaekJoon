# 20210119 복습

n, c = list(map(int, input().split()))

data = []

for _ in range(n):
    data.append(int(input()))

data.sort()

start = 1  # 1로 해야 한다 가장 작은 차이
end = data[-1] - data[0]  # 가장 큰 차이

result = 0
while start <= end:
    mid = (start + end) // 2
    value = data[0]
    k = 1

    for a in range(1, n):
        if data[a] >= value + mid:
            value = data[a]
            k += 1
    if k >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
