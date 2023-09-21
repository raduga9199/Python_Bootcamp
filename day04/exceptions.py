try:
    num = 10 / 0
    print(num)
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('finally block')

print('Test Completed')

tuple1 = (10, 20, 30, 40)

try:
    print(tuple1[2000])
except:
    print('The index number is too large')
else:
    print('The index number is invalid')

try:
    raise FileNotFoundError('No such file existing')
except SyntaxError:
    print('it is a syntax error')
except ArithmeticError:
    print('Arithmetical error')
finally:
    print('Finally block')


print('----------------------------')

raise LookupError('Invalid entry')

"""
JAVA
    throw: used for manually throwing an exception
    throws: for exception handling (as method signature)
"""
