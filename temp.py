def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("기존 데이터   :", arr)
    print("-" * 45)
    print(f"정렬 과정    : {left} + {middle} + {right}")
    return quick_sort(left) + middle + quick_sort(right)


data = [64, 34, 25, 12, 22, 11, 90]
print("정렬된 데이터 :", quick_sort(data))
