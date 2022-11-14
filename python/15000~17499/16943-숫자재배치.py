import itertools
A,B = input().strip().split()

# 먼저 가능한지 자릿수 조사
# 자릿수로 if문 하기
# 가능하면 A의 숫자를 내림차순으로 나열
# 나열 후 각 자리 수를 비교 

if len(A) > len(B):#못 만듦
    print(-1)
elif len(A) == len(B):
    #먼저 만들 수 있나 확인
    list_A =  list(map(int, A))
    list_A.sort(reverse=True)#내림차순

    #먼저 A의 가능한 조합의 수를 찾는다.
    list_result = list(itertools.permutations(list_A,len(list_A)))
    results = []
    for i in range(len(list_result)):
        number = 0
        for k in list_result[i]:
            number = 10*number + k
        results.append(number)
    
    #찾은 조합의 수로부터 B보다 작고 B와 자릿수가 같은(앞자리가 0이 아닌)
    #수를 찾는다.
    for num in results:
        if num < int(B) and len(str(num)) == len(B):
            print(int(num))
            exit()#백준에서 exit써도 됨
    print(-1)
            
elif len(A) < len(B):#A로 만들 수 있는 수 중 최대값
    list_A =  list(map(int, A))#문자열 목록을 정수로
    list_A.sort(reverse=True)
    result = ""
    for a in list_A:
        result = result + str(a)
    print(int(result))