import numbers


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}')


def sum(num1: numbers,
        num2: numbers,
        num3: numbers = 0,
        num4: numbers = 0) -> numbers:
    return num1 + num2 + num3 + num4


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0