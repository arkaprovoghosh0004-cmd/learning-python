
while True:
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  opr = input("Choose your operation (+, -, *, /): ")
  if opr == "+":
    print(num1+num2)
  elif opr == "-":
    print(num1-num2)
  elif opr == "*":
    print(num1*num2)
  elif opr == "/":
    if num2 == 0:
      print("Error: Division by zero.")
    else:
      print(num1/num2)
  else:
    print("Unknown operator.")

