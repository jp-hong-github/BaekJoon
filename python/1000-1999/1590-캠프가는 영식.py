n, t = map(int, input().split())

bus = set([])
for _ in range(n):
    temp = list(map(int, input().split()))
    for i in range(temp[2]):
        if temp[0] + i * temp[1] >= t:
            bus.add(temp[0] + i * temp[1])

data = list(bus)
data.sort()
res = []
result = 0
if len(data) == 0:
    result = t - 1
else:
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] >= t:
            end = mid - 1
            result = data[mid]
        else:
            start = mid + 1

print(result - t)
