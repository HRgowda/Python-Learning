import math
input_str = input('Enter the string (enter both alphabets and numbers): ')

only_digit = ''

for i in input_str:
  if i.isdigit():
    only_digit += str(i)

# lets check if only_digit is perfect square or not.
# Here only_digit has to be comverted to int since str and float cant be ** .

if math.ceil(math.sqrt(int(only_digit))) == math.sqrt(int(only_digit)):
  print('The number part of the given string is a perfect square hence it prints the string in reverse',input_str[::-1])
else:
  print('The number part of the given string is not a perfect square hence it prints the string itself',input_str)
