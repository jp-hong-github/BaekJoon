#그리디 알고리즘
'''
101010111
100011100

아이디어
0과 1 각각이 연속되는 횟수를 구함
예를 들어
1000111001의 경우
0은 2번
1은 3번이므로
0을 2번 뒤집으면 됨
'''
data = input()

id = [0,0]

if int(data[0])==0:
    check = 0
    for num in data[1:]:
        if int(num) != check:
            id[check]+=1
            check = 1 - check
else:
    check = 1
    for num in data[1:]:
        if int(num) != check:
            id[check]+=1
            check = 1 - check
id[check]+=1
print(min(id))