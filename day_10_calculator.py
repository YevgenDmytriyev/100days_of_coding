def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

for operation in operations:
  print(operation)
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")