x,y,w,h = input().split()
x= int(x)
y = int(y)
w = int(w)
h = int(h)
min = x
for i in [y,(w-x),(h-y)]:
    if(min>=i):
        min=i

print(min)
