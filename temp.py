def merge_sort(arr, depth=0):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    print(f"{'   ' * depth}분할 과정 {depth+1}: {left} | {right}")
    left = merge_sort(left, depth + 1)
    right = merge_sort(right, depth + 1)
    print(f"{'   ' * depth}병합 과정 {depth+1}: {left} + {right}")
    return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


data = [64, 34, 25, 12, 22, 11, 90]
print("기존 데이터   :", data)
print("-" * 45)

sorted_data = merge_sort(data)
print("-" * 45)
print("정렬된 데이터 :", sorted_data)
