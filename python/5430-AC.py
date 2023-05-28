import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    func = input().rstrip()
    n = int(input())
    errorFlag = False
    if n == 0:
        input()
        arr = []
    else:
        arr = deque(list(map(int, input().strip().lstrip("[").rstrip("]").split(","))))

    direction = "front"
    for operation in func:
        if operation == "R":
            if direction == "front":
                direction = "rear"
            else:
                direction = "front"
        else:
            if len(arr) == 0:
                errorFlag = True
                break
            else:
                if direction == "front":
                    arr.popleft()
                else:
                    arr.pop()

    if len(arr) == 0 and errorFlag:
        print("error")
    else:
        print("[", end="")
        if direction == "front":
            for i, v in enumerate(arr):
                if i == len(arr) - 1:
                    print(v, end="")
                else:
                    print(v, end=",")
        else:
            for i in range(len(arr) - 1, -1, -1):
                if i == 0:
                    print(arr[i], end="")
                else:
                    print(arr[i], end=",")
        print("]")
