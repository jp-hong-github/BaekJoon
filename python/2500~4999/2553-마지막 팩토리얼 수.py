import time

start_time = time.time()

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
            
N = int(input())
result = fac(N)
answer=0
while(1):
    if result%10 == 0:
        result = result/10
    else:
        answer = result%10
        break

print(answer)


end_time =time.time()
print(end_time-start_time)