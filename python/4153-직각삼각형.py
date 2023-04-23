import sys

input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    
    lst.sort()
    a,b,c = lst[0],lst[1],lst[2]
    if a == b == c == 0:
        break
    
    if c ** 2 == a ** 2 + b ** 2:
        print("right")
    else:
        print("wrong")

