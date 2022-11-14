n = int(input())
numbers = [int(x) for x in input().split()]

result = [0 for i in range(n)]

for i in range(n-1,-1,-1):
    for k in range(i-1,-1,-1):
        if numbers[k] <=numbers[i]:
            result[k] +=1