# Reduce the complexity and conquer

arr = [22, 11, 7, 17, 29, 3, 23, 19]
#Here 22 be the sorted array from the unsorted array.
for i in range(1, len(arr)):
  element = arr[i]
  j = i-1
  while j >= 0 and element < arr[j]:
    arr[j+1] = arr[j]
    j -= 1
  arr[j+1] = element
print(arr)



