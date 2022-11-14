import sys
import decimal
decimal.getcontext().prec = 120

input  = sys.stdin.readline
t = int(input())
cases = [decimal.Decimal(input()) for _ in range(t)]

result = []
for num in cases:
    memo = 0
    start = decimal.Decimal(0.0)
    end = num
    while abs(end-start)> decimal.Decimal(1e-14):
        mid = (start+end)/2
        value = mid**3 - num
        #print("%.5f %.5f %.5f %.5f %.5f"%(start,end,mid,value,memo))
#        if abs(value) < 1e-11:
#            memo = mid
        if value >= 0:
            end = mid
        else:
            start = mid
        memo = mid

    result.append(decimal.Decimal(memo))


for res in result:
    a = round(res,60)
    #print("%.10f"%(a))
    temp = "{0:0.13f}".format(a)
    print(temp[:-3])
    # print(res)

sys.exit(0)