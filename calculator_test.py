```python
def calculator():
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        operator = input("연산자를 입력하세요 (+, -, *, /): ")
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("오류: 0으로 나눌 수 없습니다.")
                return
            result = num1 / num2
        else:
            print("오류: 유효하지 않은 연산자입니다.")
            return

        print(f"결과: {result}")

    except ValueError:
        print("오류: 유효한 숫자를 입력하세요.")
    except Exception as e:
        print(f"알 수 없는 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    calculator()
```