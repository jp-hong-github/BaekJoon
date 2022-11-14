import sys

input = sys.stdin.readline

players = []
black = []
white = []

while True:
    try:
        temp = list(map(int, input().split()))
        break_temp = temp[0] + temp[1]
        players.append(temp)
    except:
        break

result = 0
for i in players:
    result += max(i)

print(result)
