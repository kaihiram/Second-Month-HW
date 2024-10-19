def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

# -----------------------------------

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Элемент {target} найден на индексе {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"Элемент {target} не найден"

target_element = 22
result = binary_search(sorted_list, target_element)
print(result)
