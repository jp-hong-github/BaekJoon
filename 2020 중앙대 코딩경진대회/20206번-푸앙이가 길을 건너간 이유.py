a, b, c = map(int, input().split())

x1, x2, y1, y2 = map(int, input().split())

data = [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]
data_multi = []


def function(x, y):
    return a * x + b * y + c


for i in range(4):
    data_multi.append(function(data[i][0], data[i][1]))

check = 0
for i in range(3):
    for k in range(i + 1, 4):
        if data_multi[i] * data_multi[k] < 0:
            check = 1

if check == 1:
    print("Poor")
else:
    print("Lucky")
