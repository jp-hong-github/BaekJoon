least,most = map(int,input().split())
x,y = map(int,input().split())

if least > most:
    temp = least
    least = most
    most = temp

if y >= abs(x) or y<0:
    

q_least = least//20-1
q_most = most//x
'''
1 10 
-414 442
500 20
20

'''
#print(q_least,q_most)

result = False
for q in range(q_least,q_most+1):
    if least < q*x + y and q*x + y < most:
        if result is False:
            result = q*x + y
        else:
            result = False
            break
            
if result is False:
    print("Unknwon Number")
else:
    print(result)