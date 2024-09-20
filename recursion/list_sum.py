def sum_list(num):
  
    if len(num[0]) == 0:
      return 1
    return num[0]+sum_list(num[1:])



user_input = input('Enter the numbers: ').split()
print(sum_list(user_input))

