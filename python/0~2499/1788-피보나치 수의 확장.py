n = int(input())

def fib(n):
    if n==1 or n==-1:
        return 1
    elif n==0:
        return 0
    else:
        temp0=0
        temp1=1
        result=0
        if n>=1:
            for i in range(2,n+1,1):
                result = temp0 + temp1
                temp0 = temp1
                temp1 = result
        else:
            for i in range(-2,n-1,-1):
                result = temp0 - temp1
                temp0 = temp1
                temp1 = result 
        return result

result = fib(n)

if result==0:
    print(0)
    print(0)
elif result<0:
    print(-1)
    print((0-result)%1000000000)
else:
    print(1)
    print(result%1000000000)
    
'''
1 = 0 + 1
0 = 1 + -1
1 = -1 + 2
-1 = 2 + -3
2 = -3 + 5
'''