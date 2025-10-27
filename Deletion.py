# Delete from specific position (index)

def deletion(arr, index):
    N = len(arr)
    for i in range(index, N-1):
        arr[i] = arr[i+1]

    N -= 1
    return arr[:N]




# Delete all occurences of a value

def delete_all_value(arr, item, N):
    j = 0
    for i in range(0, N-1):
        if arr[i] != item:
            arr[j] = arr[i]
            j = j + 1
    return arr[:j]



def delete_item(arr, item, N):
    for i in range(N):
        if arr[i] == item:
            for j in range(i, N-1):
                arr[j] = arr[j+1]
            N -= 1
            break
    return arr[:N]





# Example usage:
input_arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
N = len(input_arr)
input_value = int(input("Enter item to remove from it: "))
result = delete_item(input_arr, input_value, N)
print("Array after deletion:", result)





'''
input_arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
N = len(input_arr)
input_value = int(input("Enter item to remove from it: "))
delete_all_value(input_arr, input_value, N)
print("Array after deletion:", input_arr[:N-1])





input_arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
index = int(input("Enter the index to delete: "))

result = deletion(input_arr, index)
print("Array after deletion:", result)
'''