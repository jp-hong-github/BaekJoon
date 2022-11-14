# 20210119 복습

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checklist = list(map(int, input().split()))

cards.sort()


def binary_search(array, target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return 1
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in checklist:
    print(binary_search(cards, i), end=" ")


# ~ checklist를 정렬하면 안되므로 이 풀이는 불가
"""
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# 다른 풀이 : 두 리스트를 비교하며 순차적으로 탐색한다.

checklist.sort()

cards_idx = 0
checklist_idx = 0
print()
while cards_idx < n and checklist_idx < m:
    if cards[cards_idx] == checklist[checklist_idx]:
        print("1", end=" ")
        cards_idx += 1
        checklist_idx += 1
    elif cards[cards_idx] > checklist[checklist_idx]:
        print("0", end=" ")
        checklist_idx += 1
    else:
        cards_idx += 1
"""
