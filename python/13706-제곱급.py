import sys

input = sys.stdin.readline

n = int(input())
"""
해당 방법들은 float로 자동 형변환으로 인해 800자 정수를 담지 못하여 오버플로우를 발생시킴

# 첫번째 방법
print(int(n ** (1 / 2)))

# 두번째 방법
import math

print(int(math.sqrt(n)))
"""
# 세번째 방법(이분 탐색)
start = 0
end = n
while start <= end:
    mid = (start + end) // 2
    if n > mid * mid:
        start = mid + 1
    elif n == mid * mid:
        print(mid)
        break
    else:
        end = mid - 1
