n,s = map(int,input().split())

numbers = list(map(int,input().split()))

result = int(10e9)
if sum(numbers)>=s:
    for start in range(n-1):
        temp = 0
        count = 0
        for pointer in range(start,n):
            #print(pointer)
            temp+=numbers[pointer]
            count+=1
            if temp >= s and result > count:
                result = count
                break
        if result == 1:
            break

if result == int(10e9):
    print(0)
else:
    print(result)

