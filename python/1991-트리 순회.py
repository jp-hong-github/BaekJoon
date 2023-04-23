import sys
input = sys.stdin.readline 
# 이후 원래처럼 input()을 사용하면 된다

tree = {}

n = int(input())

for i in range(n):
    x,y,z = map(str,input().split())   
    tree[x] = {'left':y,'right':z}

resulta = []
resultb = []
resultc = []

def a(start):#전위 순회
    resulta.append(start)
    if tree[start]['left'] !='.':
        a( tree[start]['left'])
    if tree[start]['right'] !='.':
        a(tree[start]['right'])

def b(start):#중위 순회
    if start !='.':
        b(tree[start]['left'])
        resultb.append(start)
        b(tree[start]['right'])
    
def c(start):#후위 순회
    if start !='.':
        c(tree[start]['left'])
        c(tree[start]['right'])
        resultc.append(start)

a('A')
b('A')
c('A')
for a in resulta:
    print(a,end='')
print()
for a in resultb:
    print(a,end='')
print()
for a in resultc:
    print(a,end='')
