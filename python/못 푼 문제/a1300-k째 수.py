n = int(input())
k = int(input())

result = 0 
start = 1
end = n
while start <= end:
    mid = (start+end)//2
    print(start,end,mid)
    if mid**2 == k:
        result = mid**2
        break
    elif (mid-1)**2 < k and k < mid**2:
        temp = k - (mid-1)**2
        if temp%2==1:
            temp+=1
        result = (temp//2)*mid
        break
    elif k<=(mid-1)**2 and mid>0:
        end = mid - 1
    else:
        start = mid + 1

print("결과 : ",result)