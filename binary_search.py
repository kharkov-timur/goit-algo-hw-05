def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return iterations, arr[mid]

    if low < len(arr):
        return iterations, arr[low]
    else:
        return iterations, None


sorted_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9]
target_value = 1.4

iterations, upper_bound = binary_search(sorted_array, target_value)

print(f"Кількість ітерацій: {iterations}")

if upper_bound is not None:
    print(f"Верхня межа: {upper_bound}")
else:
    print("Елемент не знайдено.")
