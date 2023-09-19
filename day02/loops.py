s = "Python Programming"

for each in s:
    print(each)


print('----------------------------')

for i in range(0,len(s)):
    print(s[i])

print('----------------------------')

for i in range(-len(s),0):
    print(s[i])

print('----------------------------')

for i in reversed(range(-len(s),0)):
    print(s[i])

print('----------------------------')
result = ''
for x in s[::-1]:
    result += x

print(result)

print('----------------------------')

num = int(input('Enter a positive number: \n'))

while num <= 0:
    num = int(input('Enter a positive number: \n'))

print(f'You have entered {num}')