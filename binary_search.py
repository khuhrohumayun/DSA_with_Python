# Binary Search Implementation

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



# Example usage:

search_input = list(map(int, input("Enter the elements of array: ").split()))

target_value = int(input("Enter the target value to search: "))

result_index = binary_search(search_input, target_value)

if result_index != -1:
    print(f'The Element {target_value} found at index: {result_index}')
else:
    print(f'The Element {target_value} not found in the array')