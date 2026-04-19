```python
# calculator.py

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Cannot divide by zero"
  else:
    return x / y

if __name__ == "__main__":
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))

  except ValueError:
    print("Invalid input. Please enter numbers only.")
```