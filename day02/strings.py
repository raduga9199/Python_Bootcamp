name = 'Python'

print(len(name))

print(name[-6])
print(name[5])
print(name[0])

a = name[0:3]
b = name[3:6]

print(a)
print(b)

s = 'Java Programming Language'

print(s[5:16])  # slicing  [START : END]
print(s[:16])   # slicing  [      : END]
print(s[5:])    # slicing  [START :    ]
print(s[::-1])  # slicing  [  REVERSED ]

rev = 'Python Language'
print(rev)
reversed_string = reversed(rev)
for i in reversed_string:
    print(i, end="")

print()
print(s.capitalize())
print(s.title())

s = '         Python, Java          '
print(s.strip())

s = 'JAVA ABA'
s2 = 'Java Java'
print(s.index('A'))
print(s.rindex('A'))
print(s.replace('A','a'))
print(s2.replace('Java','Python'))
print(s2.replace('Java','Python',1))

s = 'C# C# Python'

print(s.replace(' C#',' Java'))
print(s.replace('C#','Java', 1))

s = 'Java Java Java Python'


