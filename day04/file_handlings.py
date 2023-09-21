path = 'files/Test.txt'

text_file = open(path, 'r')

print(text_file.read())
"""
    print(text_file.readline())
    print(text_file.readline())
    print(text_file.readline())
    print(text_file.readline())
"""
text_file.close()

print('----------------')

path = 'files/Test2.txt'
text_file = open(path, 'w')

text_file.write('This is a new text file created with Python')

text_file.close()
