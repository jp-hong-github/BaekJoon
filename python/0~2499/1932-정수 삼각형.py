n = int(input())

tri = []
for i in range(n):
    tri.append(list(map(int,input().split())))
    

for i in range(1,n):
    for k in range(i+1):
            if k==0:
                tri[i][k] = tri[i][k] + tri[i-1][k]
            elif k==i:
                tri[i][k] = tri[i][k]+ tri[i-1][k-1]
            else:
                tri[i][k] = tri[i][k] + max(tri[i-1][k], tri[i-1][k-1])

    # for i in tri:
    #     print(i)
print(max(tri[n-1]))