def bin2dec(val):
 return int(val,2)
def oct2hex(val):
 return hex(int(val,8))
try:
 num1=input("enter a binary number")
 print(bin2dec(num1))
except ValueError:
 print("Invalid literal in input with base2")
try:
 num2=input("enter a octal number")
 print(oct2hex(num2))
except ValueError:
 print("Invalid literal in input with base8")

# def F(n):
#  if n<0:
#   print("incorrect input")
#  elif(n==0):
#   return 0
#  elif(n==1 or n==2):
#   return 1
#  else:
#   return F(n-1)+F(n-2)
# num=int(input("enter a number:"))
# print(F(num))

# decimal_number = int(input())
# binary_number = bin(decimal_number)
# octal_number = oct(decimal_number)
# hexadecimal_number = hex(decimal_number)

# print("Decimal:    ", decimal_number)
# print("Binary:    ", binary_number) # Remove the '0b' prefix
# print("Octal:      ", octal_number) # Remove the '0o' prefix
# print("Hexadecimal:", hexadecimal_number)
 