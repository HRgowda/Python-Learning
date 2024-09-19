def demo(arr, k):
  n = len(arr)
  
  k = k % n
  
  for _ in range(k):
    temp = arr[0]
    
    for i in range(n-1):
      arr[i] = arr[i+1]
      
    arr[n-1] = temp
    
  return arr
  # return arr[k:] + arr[:k]
    
arr = [1,2,3,4,5,6,7]
demo(arr, 2)
