#Accept a string of Pairs of Peranthesis and check if they are arranged properly. If so, print the number of pairs of peranthesis else print improper arrangement.

# Method 1
user_input = input('Enter the parenthesis: ')
paranthesis_list = []
count = 0

for i in user_input:
        if i == '(':
            paranthesis_list.append(i)
        elif i == ')' and paranthesis_list:
            paranthesis_list.pop()
            count += 1
        else:
            print("Improper arrangement")

if not paranthesis_list:
   print(f"Number of pairs of parentheses: {count}")
else:
   print("Improper arrangement")
   

# Method 2
user_input = input('Enter the paranthesis: ')

open_paranthesis = 0

close_paranthesis = 0

arrangement = True

for char in user_input:
  
  if char != ')' and char != '(':
    print('Invalid input.')
    exit(0)
    
  if char == '(':
    open_paranthesis += 1
    
  elif char == ')':
    close_paranthesis += 1
    
  if close_paranthesis > open_paranthesis:
    print('Invalid arrangement.')
    arrangement = False
    break
  
if arrangement and open_paranthesis == close_paranthesis:
  print('The number of pair of paranthseis is',open_paranthesis)
else:
  print('INvalid')
