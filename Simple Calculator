# Simple Python Calculator

# takes two numbers and an operator
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
operator = input("Enter an operator: ")

if operator == "+":
  result = num1+num2
elif operator == "-":
  result = num1-num2
elif operator == "*":
  result = num1*num2
elif operator == "/":
  if num2 == 0:
    print("0 can't be divided.")
    result = None
  else:
    result = num1/num2
else:
  print("Please enter a correct operator.")
  result = None

if result != None:
  print(f"The result of {num1} {operator} {num2} is {result}")
