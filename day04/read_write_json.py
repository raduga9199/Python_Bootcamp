import json

path = 'files/Test.json'

jason_file = open(path, 'r')

dictionary = json.load((jason_file))

print(dictionary)
print(type(dictionary))

for x in dict(dictionary).keys():
    print(x)

jason_file.close()

students = {
    'S1': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subject': ['Math', 'Physics']
    },
    'S2': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subject': ['Biology', 'Programming']
    },
    'S3': {
        'name': 'Yulia',
        'gender': 'Male',
        'gpa': 4,
        'subject': ['Chemistry', 'Programming']
    },
}

dictionary['name'] = 'Aaron King'
dictionary['age'] = 45

print(dictionary)

jason_file = open('files/Test2.json', 'w')

json_object = json.dumps(students, indent=2)

jason_file.write(json_object)
