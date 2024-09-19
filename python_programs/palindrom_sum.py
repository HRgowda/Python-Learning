input_str = input('Enter the string (enter both alphabets and numbers): ')

characters = ''
numbers = ''

for i in input_str:
  if i.isalpha():
    characters += str(i)
  else:
    numbers += str(i)
print(characters)

if characters[::-1] == characters:
  sum = 0
  for num in numbers:
    sum += int(num)**2
  print('Since the alphabet part of the string is a Palindrome,it prints sum of the squares of the digits in the number part of the string =',sum)
else:
  sum=0
  for num in numbers:
    sum += int(num)
  print('Since the alphabet part of the string is not a Palindrome,it prints sum of the digits in the number part of the string =',sum)

