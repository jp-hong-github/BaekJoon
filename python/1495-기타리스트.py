import sys
input = sys.stdin.readline

n,s,m = map(int,input().split())

vol = list(map(int,input().split()))

dp = []
check = 0
for case in range(len(vol)):
    temp= []
    if case == 0 :
        if s - vol[case] <0:
            #temp.append(-1)
            a=1
        else:
            if s - vol[case] not in temp:
                temp.append(s - vol[case])
        if  s + vol[case] >m:
            #temp.append(-1)
            a=1
        else:
            if s + vol[case] not in temp:
                temp.append(s + vol[case])
        if len(temp)!=0:
            dp = temp
        else:
            check = -1
            break
    else:
        for pre in dp:
            if pre - vol[case] <0:
                #temp.append(-1)
                a=1
            else:
                if pre - vol[case] not in temp:
                    temp.append(pre - vol[case])
            if  pre + vol[case] >m:
                #temp.append(-1)
                a=1
            else:
                if pre + vol[case] not in temp:
                    temp.append(pre + vol[case])
        if len(temp)!=0:
            dp = temp
        else:
            check = -1
            break
if check == -1:
    print(-1)
else:
    print(max(dp))