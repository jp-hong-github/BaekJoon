num = int(input())
nlist = []
for i in range(num):
    nlist.append(input().strip().split("X"))

for i in range(num):
    sum = 0
    for k in nlist[i]:
        sum += (len(k) * (len(k) + 1)) / 2
    print(int(sum))
