n = int(input())

data  = set([])
for i in range(n):
    text = input()
    data.add((len(text),text))

data = list(data)
data.sort()

for i in range(len(data)):
    print(data[i][1])