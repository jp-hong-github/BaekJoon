import sys
from collections import deque

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

s = list(s)
t = deque(list(t))

# 값이 -1이면 뒤에서 리스트 값을 제거
# 값이 0이면 앞에서 리스트 값을 제거
direction = -1

# 문자열의 뒤에서 A를 제거한다
# 문자열의 뒤에서 B를 제거한 후 뒤집는다


while len(t) > len(s):
    if direction == -1:
        v = t.pop()
        if v == "B":
            direction = 0
    else:
        v = t.popleft()
        if v == "B":
            direction = -1


if direction == 0:
    t.reverse()


for i in range(len(t)):
    if t[i] != s[i]:
        print(0)
        sys.exit()

print(1)
