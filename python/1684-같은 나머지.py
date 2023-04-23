import sys
import math

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

# N_1 - Q_1 x D = N_2 -Q_2 x D = R
# N_1 - N_2 = D x (Q_2 - Q_1)
# D는 N_1 - N_2의 약수

num_list.sort()
diff = [num_list[i + 1] - num_list[i] for i in range(len(num_list) - 1)]

result = math.gcd(*diff)
print(result)

