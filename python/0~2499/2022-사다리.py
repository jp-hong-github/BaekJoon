x,y,c = map(float,input().split())

start= 0
end = min(x,y)
result= 0 
def f(mid):
    X = (x**2 - mid**2)**0.5
    Y = (y**2 - mid**2)**0.5
    return X*Y/(X+Y)
    
while  end - start > 1e-4:
    mid  = (start+end)/2
    temp = f(mid)
    if temp>=c:
        result = mid
        start = mid
    else:
        end = mid

print(result)