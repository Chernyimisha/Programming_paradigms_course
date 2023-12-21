def binary_search(array: list[int], number: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        middle = array[mid]
        if middle < number:
            left = mid + 1
        elif middle > number:
            right = mid - 1
        else:
            return mid
    return -1


arr = [12, 24, 32, 39, 45, 50, 54]
n = 24

result = binary_search(arr, n)

print(result)