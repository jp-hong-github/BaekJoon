t = int(input())

dRow = [1,1,2,2,-1,-1,-2,-2]
dCol = [-2,2,-1,1,-2,2,-1,1]

from collections import deque

for _ in range(t):
    i = int(input())
    cRow,cCol = map(int,input().split())
    fRow,fCol = map(int,input().split())
    if cRow == fRow and cCol == fCol:
        print(0)
        continue
    
    q= deque()
    q.append((cRow,cCol,0))
    stop = 0
    board = [[0 for _ in range(i)]for __ in range(i)]
    board[cRow][cCol] = 1
    while q:
        row,col,num = q.popleft()
        
        for z in range(8):
            nRow = dRow[z] + row
            nCol = dCol[z] + col
            
            if nRow < 0 or nRow >=i or nCol < 0 or nCol>=i:
                continue
            if nRow == fRow and nCol == fCol:
                print(num+1)
                stop=1
                break
            if board[nRow][nCol] == 1:
                continue
            else:
                board[nRow][nCol] = 1
                q.append((nRow,nCol,num+1))
                #print(nRow,nCol)
        
        if stop==1:
            break
