num = int(input())
nlist = []
for i in range(num):
    nlist.append([int(x) for x in input().strip().split()])

for i in range(num):
    avg = (sum(nlist[i]) - nlist[i][0]) / nlist[i][0]
    # sum(nlist[i][1:]) 이렇게 해도 됨
    print(
        "%.3lf%s" % (len([x for x in nlist[i][1:] if x > avg]) / nlist[i][0] * 100, "%")
    )
    # list comprehesion 사용
    # round() 함수로도 소수점 반올림 가능
