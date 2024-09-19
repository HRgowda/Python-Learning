user_input = int(input('Enter a 4 digit number(dont repeat the same number twice): '))

count = 0

while True:
  if user_input == 6174:
    print('The entered number is a Karpekar number.')
    exit(0)
  if len(str(user_input)) < 4 :
    print('Ivalid input entered, number must contain atleast 4 digits.')
    exit(0)
    
  ascending = ''.join(sorted(str(user_input)))
  
  descending = ''.join(sorted(str(user_input), reverse=True))
  
  difference = int(descending) - int(ascending)
  
  print(f'{descending}-{ascending}={difference}')
  
  user_input = difference
  
  count += 1
  
  if difference == 6174:
    print('The logic was implemented '+str(count)+' times to get Karpekar\'s constant.')
    break
