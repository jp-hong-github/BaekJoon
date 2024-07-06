def bubble_sort(arr):
    n = len(arr)
    print("Original array:", arr)
    for i in range(n):
        print(f"Step {i+1}: ", end="")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
    return arr


# 예제
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)
