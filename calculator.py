# calculator.py

def add(x, y):
  """Adds two numbers."""
  return x + y

def subtract(x, y):
  """Subtracts the second number from the first."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides the first number by the second."""
  if y == 0:
    return "Error: Cannot divide by zero!"
  return x / y

if __name__ == "__main__":
  print("--- Simple Calculator ---")

  # Example calculations
  num1 = 10
  num2 = 5

  print(f"{num1} + {num2} = {add(num1, num2)}")
  print(f"{num1} - {num2} = {subtract(num1, num2)}")
  print(f"{num1} * {num2} = {multiply(num1, num2)}")
  print(f"{num1} / {num2} = {divide(num1, num2)}")

  num3 = 10
  num4 = 0
  print(f"{num3} / {num4} = {divide(num3, num4)}")

  print("-----------------------")