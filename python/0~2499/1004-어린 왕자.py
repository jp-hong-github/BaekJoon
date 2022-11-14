import sys

input = sys.stdin.readline

T = int(input())


def check_planet(x, y, c_x, c_y, r):
    dist = (x - c_x) ** 2 + (y - c_y) ** 2
    r_2 = r ** 2
    if dist < r_2:
        return True
    else:
        return False



result_lst=[]
for _ in range(T):
    result = 0
    
    start_x, start_y, dest_x, dest_y = map(int, input().split())
    n = int(input())
    for __ in range(n):
        c_x, c_y, r = map(int, input().split())
        # 출발점 또는 도착점이 행성계에 포함하는지
        start_check = check_planet(start_x, start_y, c_x, c_y, r)
        end_check = check_planet(dest_x, dest_y, c_x, c_y, r)
        if start_check and not end_check:
            result += 1
        if not start_check and end_check:
            result += 1
    result_lst.append(result)
    
for result in result_lst:
    print(result)
