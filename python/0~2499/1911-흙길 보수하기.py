import sys

input = sys.stdin.readline

N, L = map(int, input().split())


pools_of_water = []
for _ in range(N):
    pools_of_water.append(list(map(int, input().split())))

pools_of_water.sort(key=lambda x: [x[0], x[1]])
result = 0

for i in range(N):
    result += (pools_of_water[i][1] - pools_of_water[i][0]) // L
    rest = (pools_of_water[i][1] - pools_of_water[i][0]) % L

    if rest:
        if i != N - 1:
            cur_pointer = pools_of_water[i][1] + (L - rest)
            if pools_of_water[i + 1][0] <= cur_pointer:
                pools_of_water[i + 1][0] = cur_pointer
        result += 1


print(result)
