import numbers


def display_message():
    print('Hello Cydeo')
    print('Hello World')

display_message()

def value_integer():
    return 10


def value_string():
    return 'Hello World'


print(value_integer())
print(value_string())


def return_int() -> int:
    return 20


print(return_int())


def divide(num1, num2):
    return num1 / num2


print(divide(20,2))
#  print(divide('20','2'))


def square(num: int):
    return num * num


print(square(10))
# print(square('Java'))


def add(num1: int, num2: int):
    return num1 + num2


print(add(10,20))


def add_numbers(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(add_numbers(10.5, 20.5))
print('------------------------------------------------')


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


print(calculate(10, 4, '-'))
print(calculate(10, 4, '+'))
print(calculate(10, 4, '/'))
print(calculate(10, 4, '*'))
print('------------------------------------------------')


def sum(num1: numbers,
        num2: numbers,
        num3: numbers = 0,
        num4: numbers = 0) -> numbers:
    return num1 + num2 + num3 + num4


print(sum(1, 2))
print(sum(1, 2, 3))
print(sum(1, 2, 3, 4))


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}')


concat('Cydeo','School')