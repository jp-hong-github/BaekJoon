n = int(input())

data = list(map(int,input().split()))

array = [1] * n

for i in range(n-1):
    for k in range(i+1,n):
        if data[k]>data[i]:
            if array[k]<array[i]+1:
                array[k] = array[i]+1

print(max(array))