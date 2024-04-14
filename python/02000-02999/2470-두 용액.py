n = int(input())
data = list(map(int, input().split()))
data.sort()


result1 = 0
result2 = 0
value = 9999999999999999
for i in range(0, n):
    start = i + 1
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        # print("i : %d,start : %d,end : %d,mid : %d, value : %d"%(i,start,end,mid,data[i] + data[mid]))
        if abs(data[i] + data[mid]) < abs(value):
            value = data[i] + data[mid]
            result1, result2 = data[i], data[mid]
            if value == 0:
                break
            elif value < 0:
                start = mid + 1
            else:
                end = mid - 1
        elif data[i] + data[mid] > value:
            end = mid - 1
        else:
            start = mid + 1

print(result1, result2)
