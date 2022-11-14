t = int(input())
a=[]
for i in range(t):
    h,w,n = input().split()
    a.append(int(h))
    a.append(int(w))
    a.append(int(n))

for i in range(t):
    if(a[i*3+2]%a[i*3]!=0):
        print(a[i*3+2]%a[i*3]*100 + a[i*3+2]//a[i*3]+1)
    else:
        print(a[i*3]*100 + a[i*3+2]//a[i*3])
