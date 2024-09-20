def factorial(num):
  if num == 1 or num == 0:
    return 1
  return num*factorial(num-1)

user_input = int(input('Enter a number to find it\'s Factorial: '))

print(f'Factorial {user_input} is {factorial(user_input)}')

