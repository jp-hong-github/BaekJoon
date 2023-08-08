"""
10 30 40
40 + 80 =120
70 + 80 = 150
"""
"""
우선순위 큐 => heapq로 구현
"""

import heapq

n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

heapq.heapify(numbers)

result = 0
while len(numbers) >= 2:
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)
    heapq.heappush(numbers, a + b)
    result += a + b

print(result)
