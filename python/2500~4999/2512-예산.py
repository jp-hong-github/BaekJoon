n = int(input())
yesan = list(map(int,input().split()))
total = int(input())
start = 1
end = max(yesan)
result= 0
while start<=end:
    mid = (start+end) //2
    sum_yesan = 0
    for p in yesan:
        if p>mid:
            sum_yesan+=mid
        else:
            sum_yesan+=p
    
    if sum_yesan > total:
        end = mid-1
    else:
        result = mid
        start = mid +1

print(result)
            