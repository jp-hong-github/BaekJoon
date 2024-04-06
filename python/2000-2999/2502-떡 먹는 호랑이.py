import sys

input = sys.stdin.readline

D, K = map(int, input().split())

fibonacci = [0, 1, 1]

for i in range(3, 30):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

# x*A + y*B = K
x = fibonacci[D - 2]
y = fibonacci[D - 1]
A, b = 0, 0

for b in range(50000, 0, -1):
    if (K - y * b) >= 1 and (K - y * b) % x == 0:
        if (K - y * b) // x <= b:
            A = (K - y * b) // x
            B = b
            break
print(A)
print(B)
