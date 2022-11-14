import sys
input = sys.stdin.readline

n = int(input()) #<100

graph = [[0 for _ in range(n+1)] for __ in range(n+1)]

appleNum = int(input())

for i in range(appleNum):
    row,col = map(int,input().split()) 
    graph[row][col] = 1


change = []
changeNum = int(input())
for i in range(changeNum):
    time,direction = map(str,input().split()) 
    change.append([int(time),direction])

from collections import deque
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
q = deque([[1,1,RIGHT]])

graph[1][1] = 100 # 뱀이 있는 곳
time = 0 

change_idx = 0
cRow,cCol,go = 1,1,RIGHT
while q:
    time+=1
    if go == RIGHT:
        cCol += 1
        if cCol <=0 or cCol > n or graph[cRow][cCol] == 100:
            print(time)
            break
        elif graph[cRow][cCol] == 1:
            q.appendleft([cRow,cCol,go])
            graph[cRow][cCol] = 100
        else:
            temp = q.pop()
            pre_col,pre_row,pre_go = temp[0],temp[1],temp[2]
            graph[pre_col][pre_row] = 0
            q.appendleft([cRow,cCol,go])
            graph[cRow][cCol] = 100
    elif go == DOWN:
        cRow += 1
        if cRow <=0 or cRow > n or graph[cRow][cCol] == 100:
            print(time)
            break
        elif graph[cRow][cCol] == 1:
            q.appendleft([cRow,cCol,go])
            graph[cRow][cCol] = 100
        else:
            temp = q.pop()
            pre_col,pre_row,pre_go = temp[0],temp[1],temp[2]
            graph[pre_col][pre_row] = 0
            q.appendleft([cRow,cCol,go])
            graph[cRow][cCol] = 100
            
    elif go == LEFT:
        cCol += -1
        if cCol <=0 or cCol > n or graph[cRow][cCol] == 100:
            print(time)
            break
        elif graph[cRow][cCol] == 1:
            q.appendleft([cRow,cCol,go])
            graph[cRow][cCol] = 100
        else:
            temp = q.pop()
            pre_col,pre_row,pre_go = temp[0],temp[1],temp[2]
            graph[pre_col][pre_row] = 0
            q.appendleft([cRow,cCol,go])
            graph[cRow][cCol] = 100
            
    elif go == UP:
        cRow += -1
        if cRow <=0 or cRow > n or graph[cRow][cCol] == 100:
            print(time)
            break
        elif graph[cRow][cCol] == 1:
            q.appendleft([cRow,cCol,go])
            graph[cRow][cCol] = 100
        else:
            temp = q.pop()
            pre_col,pre_row,pre_go = temp[0],temp[1],temp[2]
            graph[pre_col][pre_row] = 0
            q.appendleft([cRow,cCol,go])
            graph[cRow][cCol] = 100
            
    if change_idx<= len(change)-1 and time == change[change_idx][0]:
        if change[change_idx][1] == 'D':
            go= (go+1)%4
        else:
            go= (go-1)%4
        change_idx+=1

    #print("cRow : ",cRow,"cCol : ",cCol,"time : ",time)
