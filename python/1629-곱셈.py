import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())


def cal(a,b):
    if b==1:
        return a%c
    
    value = cal(a,b//2)
    if b%2==0:
        return (value * value)%c
    else:
        return (value * value * a)%c 
    
print(cal(a,b))