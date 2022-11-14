n,m = map(int,input().split())

data = []
for i in range(n):
    data.append(int(input()))
    

start = 1
end = max(data) * m
result = 9999999999999999999
while start <= end:
    mid = (start+end)//2
    case = 0 
    for k in data:
        value = mid//k
        case += value
    if case < m:
        start = mid + 1
    else:
        if result > mid:
            result = mid
        end = mid - 1
    #print(start,end,mid,case)

print(result)