import sys
input =sys.stdin.readline

n,m= map(int,input().split())

know_true = list(map(int,input().split())) #0번째는 진실을 아는 사람의 수
party=[]

if know_true[0] == 0:
    #어차피 진실을 아는 사람이 없으므로 그냥 값만 입력받는다
    for _ in range(m):
        list(map(int,input().split()))
    print(m)
else:
    know_true_num = know_true.pop(0) # 진실을 아는 사람의 수
    know_true = set(know_true)  
    for _ in range(m):
        temp = list(map(int,input().split())) # n번째 파티에 관한 정보
        set_temp = set(temp[1:])
        if set_temp & know_true:
            know_true = know_true | set_temp
        else:
            party.append(set_temp)
    
    length = len(party)
    i=0
    while i<length:
        if party[i] & know_true:
            know_true = know_true | party[i]
            del party[i]
            i=0
            length-=1
        else:
            i+=1
        #print(i,length,party,know_true)
    print(len(party))