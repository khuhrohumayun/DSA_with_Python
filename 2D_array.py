

# sum of diognal elements using 1 for loop
arr = [
    [44, 55, 12, 65, 12],
    [44, 76, 12, 65, 12],
    [44, 55, 12, 65, 12],
    [44, 55, 12, 65, 12],
    [44, 55, 12, 65, 12]
]

row = 5
sum = 0

for i in range(row):
        sum += arr[i][i]


print(sum)



# Sum of index if they are even then put the zero on that cell


arr = [
    [3, 5, 1, 6, 2],
    [1, 6, 3, 6, 9],
    [9, 5, 3, 6, 7],
    [7, 8, 1, 6, 1],
    [3, 5, 2, 5, 3]
]

row = len(arr)
col = len(arr[0])

for row in range(5):
      for col in range(5):
            if (row + col) % 2 == 0:
                  arr[row][col] = 0


for row in arr:
    print(row, sep= '')




# Consider 2D array we need to find the mean row by row.

arr = [
    [3, 5, 1, 6, 2],
    [1, 6, 3, 6, 9],
    [9, 5, 3, 6, 7],
    [7, 8, 1, 6, 1],
    [3, 5, 2, 5, 3]
]

row = len(arr)
col = len(arr[0])

B = []

for i in range(row):
      temp = 0
      for j in range(col):
            temp += arr[i][j]

      avg = temp / col
      B.append(avg)


print("Mean of each Row:", B)


print('\n')

# Consider the 2D array size nxn required the interchange the upper and lower diognal.

arr = [
    [13, 15, 11, 36, 20],
    [10, 16, 13, 16, 99],
    [90, 15, 32, 26, 77],
    [70, 81, 15, 61, 11],
    [30, 15, 28, 15, 33]
]


print("Inter-Change the upper and lower diognal: ")
row = len(arr)
col = len(arr[0])

for i in range(row):
      for j in range(col):
            if i < j:
                temp = arr[i][j]
                arr[i][j] = arr[j][i]
                arr[j][i] = temp
        


for row in arr:
      print(row)




# Inter-Change teh upper and lower using 1 loop

arr = [
    [13, 15, 11, 36, 20],
    [10, 16, 13, 16, 99],
    [90, 15, 32, 26, 77],
    [70, 81, 15, 61, 11],
    [30, 15, 28, 15, 33]
]


print("Inter-Change the upper and lower diognal: ")
n = len(arr)

for k in range(n*n):
      i = k // n
      j = k % n

      if i < j:
            temp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = temp


for row in arr:
      print(row)
