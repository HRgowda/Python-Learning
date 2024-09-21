arr =  [22, 11, 7, 17, 29, 3, 23, 19]

for i in range(len(arr)):
  min_ind = i
  for j in range(i+1, len(arr)):
    if arr[j] < arr[min_ind]:
      temp = arr[j]
      arr[j] = arr[min_ind]
      arr[min_ind] = temp
      print(arr)
print(arr)

