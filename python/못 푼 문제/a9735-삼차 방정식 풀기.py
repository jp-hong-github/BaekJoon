#뉴턴랩습법 사용
n = int(input())

eq = []
result=[]

def f(a,b,c,d,x):
    return a*x**3 + b*x**2 + c*x + d

def f_p(a,b,c,x):
    return 3*a*x**2 + 2*b*x + c

for i in range(n): 
    eq.append(list(map(int,input().split())))
    
    
for i in range(n):
    a = eq[i][0]
    b = eq[i][1]
    c = eq[i][2]
    d = eq[i][3]
    valueInRoot = b**2 -a*c
    if valueInRoot>0:
        result = []
        #5가지 경우가 있다.
        if a>0:
            x_p_1 = (-b+valueInRoot**0.5)/(3*a) # 큰 값
            x_p_2 = (-b-valueInRoot**0.5)/(3*a) # 작은 값
            if f(a,b,c,d,x_p_1)>0 and f(a,b,c,d,x_p_2)>0:
                x=x_p_2-1
            elif f(a,b,c,d,x_p_1)==0 and f(a,b,c,d,x_p_2)>0:
                result.append(x_p_1)
                x=x_p_2-1
            elif f(a,b,c,d,x_p_1)<0 and f(a,b,c,d,x_p_2)>0:
                #해가 3개
                pass
            elif f(a,b,c,d,x_p_1)<0 and f(a,b,c,d,x_p_2)==0:
                result.append(x_p_2)
                x=x_p_1+1
            elif f(a,b,c,d,x_p_1)<0 and f(a,b,c,d,x_p_2)<0:
                x=x_p_1+1
                
        elif a<0:
            x_p_2 = (-b+valueInRoot**0.5)/(3*a) # 큰 값
            x_p_1 = (-b-valueInRoot**0.5)/(3*a) # 작은 값
            if f(a,b,c,d,x_p_1)>0 and f(a,b,c,d,x_p_2)>0:
                x=x_p_2-1
            elif f(a,b,c,d,x_p_1)==0 and f(a,b,c,d,x_p_2)>0:
                result.append(x_p_1)
                x=x_p_2-1
            elif f(a,b,c,d,x_p_1)<0 and f(a,b,c,d,x_p_2)>0:
                #해가 3개
                pass
            elif f(a,b,c,d,x_p_1)<0 and f(a,b,c,d,x_p_2)==0:
                result.append(x_p_2)
                x=x_p_1+1
            elif f(a,b,c,d,x_p_1)<0 and f(a,b,c,d,x_p_2)<0:
                x=x_p_1+1

    
    #해가 하나인 경우
    elif valueInRoot == 0:
        x=0
        previous_x = 0
        f_p_0_x = -b/(3*a)
        if f_p_0_x == float(x):
            print("0.0000")
        else:
            while True:
                f = f(a,b,c,d,x)
                f_p = f_p(a,b,c,x)
                i+=1
                previous_x = x
                x = float(x) - float(f)/float(f_p)
                if abs(x-previous_x)<0.0001:
                    break
            print("%.4f"%(x))
    else:
        x=0
        previous_x = 0
        i=0
        while True:
            f = f(a,b,c,d,x)
            f_p = f_p(a,b,c,x)
            i+=1
            previous_x = x
            x = float(x) - float(f)/float(f_p)
            if abs(x-previous_x)<0.0001:
                break
        print("%.4f"%(x))
        
