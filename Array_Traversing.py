
            # Print the element of array using the index

# array = [10, 20, 30, 40, 50]
# print("Array elements:")
# for index in range(len(array)):
#     print(index, ":" , array[index])


    # Cumulative sum of array elements
'''
array = [10, 20, 30, 40, 50]
sum = 0 
for element in array:
    sum += element

print("Cumulative sum:", sum)
'''


    # Sum of elements at even indices
'''
arr = [45, 78, 12, 67, 55, 89]
sum = 0
#  for index in range(0, len(arr), 2):  This is also correct way to do it.. 
for index in range(len(arr)):
    if index % 2 == 0:
        sum += arr[index]   

print("Sum of elements at even indices:", sum)  
'''


'''
            # Find the maximum element in an array

arr = [45, 78, 12, 67, 55, 89]
max_element = arr[0]  # Assume the first element is the maximum
for element in arr:
    if element > max_element:
        max_element = element
print("Maximum element in the array:", max_element)

            # Find the minimum element in an array

arr = [45, 78, 12, 67, 55, 89]
min_element = arr[0] # Assume the first element is the minimum
for element in arr:
    if element < min_element:
        min_element = element

print("Minimum element in the array:", min_element)

'''


'''
            # Linear Search in an array

arr = [45, 78, 12, 67, 55, 89]
target = 12
found = False
for index in range(len(arr)):
    if arr[index] == target:
        print(f'The Element {target} found at index: {index}') 
        found = True
        break

if not found:
    print(f'The Element {target} not found in the array')

'''


            # Bubble Sort Algorithm

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
n = len(arr)

print("Original array is:", arr)

for i in range(n-1):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array is:", arr)