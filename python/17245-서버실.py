n = int(input())
data = []
total = 0
end = 0
for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
    total += sum(temp)
    end = max(end, max(temp))

start = 1
if total % 2 == 0:
    half = total // 2
else:
    half = total // 2 + 1
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(n):
        for k in range(n):
            if mid >= data[i][k]:
                count += data[i][k]
            else:
                count += mid

    if count >= half:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
    # print(start,end,mid,count)
# print(half)
print(result)
