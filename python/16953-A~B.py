a,b = map(int,input().split())
i=0
while a<b:
    
    if b%2 == 0:
        b = b//2
    elif b%10==1:
        b = b//10
    else:
        break
    i+=1

if a==b:
    print(i+1)
else:
    print(-1)
    