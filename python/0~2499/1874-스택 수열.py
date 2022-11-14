import sys

input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

stack = []
idx = 0  # numbers를 가리키는 인덱스
current_value = 1  # <= n
top = -1  # 스택의 최상위를 가리키는 인덱스
result = []
flag = True
while True:
    if (top == -1 or stack[top] != numbers[idx]) and current_value <= n:
        stack.append(current_value)
        current_value += 1
        top += 1
        result.append("+")
    elif stack[top] == numbers[idx]:
        stack.pop()
        top -= 1
        idx += 1
        result.append("-")
        if idx == n:
            break
    else:
        flag = False
        break

if flag:
    for c in result:
        sys.stdout.write(c + "\n")
else:
    print("NO")
