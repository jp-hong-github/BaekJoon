num = int(input())
nlist = [int(x) for x in input().strip().split()]
#이렇게 하면 한줄에 여러 정수 입력 가능
#split()은 공백을 기준으로 문자열을 분리한다.
# strip()은 양쪽 끝 공백을 제거. 이거 없어도 됨
# a = list(map(int, input().strip().split()))
'''
for _ in range(2):
    a = list(map(int, input().split()))
    print(a)
    이렇게도 가능
'''
print(min(nlist),end = ' ')
print(max(nlist))
