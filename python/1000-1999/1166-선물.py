import sys
from decimal import *

input = sys.stdin.readline

N, L, W, H = map(str, input().split())
N, L, W, H = Decimal(N), Decimal(L), Decimal(W), Decimal(H)

start = Decimal("0")
end = min(L, W, H)

mid = (start + end) / 2
# result = 0
while start < end:
    mid = (start + end) / 2
    num = (L // mid) * (W // mid) * (H // mid)  # 상자에 넣을 수 있는 최대 개수 계산
    # print(start, end, num)
    if num >= N:
        start = mid + Decimal("0.00000000001")
        # result = mid
    else:
        end = mid - Decimal("0.00000000001")

print(mid)
