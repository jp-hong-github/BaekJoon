import sys

input = sys.stdin.readline


N = int(input())
meeting = []
for i in range(N):
    meeting.append(list(map(int, input().split())))

meeting.sort(key=lambda x: [x[1], x[0]])
last = meeting[0][1]
count = 1

for start, end in meeting[1:]:
    if start >= last:
        count += 1
        last = end

print(count)
