```python
def multiply_numbers():
  """두 숫자를 입력받아 곱하는 함수."""

  try:
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    product = num1 * num2
    print("두 수의 곱은:", product)
  except ValueError:
    print("잘못된 입력입니다. 숫자를 입력해주세요.")

if __name__ == "__main__":
  multiply_numbers()
```