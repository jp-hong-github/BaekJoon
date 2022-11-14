'''
L과 R이 주어진다. 이때, L보다 크거나 같고,
R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에
들어있는 8의 개수를 구하는 프로그램을 작성하시오.


L <= 2,000,000,000
L <= R <= 2,000,000,000


L과 R의 자릿수가 바뀌면 무조건 0일수밖에 없다

elif는 아예 L R이 같을 때 8이 있는 경우 또는 없는 경우
else문은 자릿수가 같으면?
430 438
808 898

88887788 88889658
'''


L,R = input().strip().split()

if len(L) < len(R):
    print(0)
elif L == R:
    print(L.count('8'))
    
else:
    result = 0
    for idx in range(len(L)):
        if L[idx] == R[idx]:#자릿수의 숫자가 같은 때
            if L[idx]=='8':#하필 그 숫자가 8일 때
                result+=1
        else:
            break
    print(result)
    
