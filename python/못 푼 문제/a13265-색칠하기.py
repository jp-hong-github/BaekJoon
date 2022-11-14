t = int(input())

def dfs(current,circle_color,lines,color):
    circle_color[current] = color
    for next in lines[current]:
        if circle_color[next]!=0:
            dfs(next,circle_color,lines,color)

for _ in range(t):
    n,m=map(int,input().split())
    lines = [[] for _ in range(n+1)]
    for _ in range(m):#양뱡향임
        x,y = map(int,input().split())
        lines[x].append(y)
        lines[y].append(x)
    circle_color = [0]*(n+1) #각 원마다 어떤 색깔인지 저장 사실상 visited 역할
    color = 1
    while True:
        for check_color in circle_color[1:]:
            if check_color == 0:
                dfs(check_color,circle_color,lines,color)
                color+=1
            
            
            