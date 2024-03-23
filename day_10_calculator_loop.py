from replit import clear

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def start_calculation():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation: ") 
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)
  clear()
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  return first_answer

answer = start_calculation()

while True:
  choice1 = input("Please make your choice: 'y' to continue, 'n' to start new, or 'q' to quit\n")
  if choice1 == 'y':
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation: ")
    calculation_funk = operations[operation_symbol]
    b = float(input("What's the next number?: "))
    answer = calculation_funk(answer, b)
    clear()
    print(f"{answer} {operation_symbol} {b} = {answer}")
  elif choice1 == 'n':
    answer = start_calculation()
  elif choice1 == 'q':
    break
