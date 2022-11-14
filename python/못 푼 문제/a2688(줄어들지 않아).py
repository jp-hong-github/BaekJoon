num_of_test_case = int(input())
test_case =[]

for i in range(0,num_of_test_case):
    test_case.append(int(input()))

n_case = {1:10}#각 경우를 저장하는 딕셔너리

for i in test_case:
    if i in n_case:
        print(n_case[i])
    elif i not in n_case:
        for k in range(i,0,-1):
            if k in n_case:
                break    
        

for k in range(10,1,-1):
    print(k)
    
'''
0~9 : 10
10+9+1 = 55
55 

'''