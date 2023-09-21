employee1 = {}

employee1['name'] = 'James'
employee1['name'] = 'Daniel'
employee1['age'] = 45
employee1['salary'] = 60_000

print(employee1)

employee2 = {
    'name': 'James',
    'age': 29,
    'salary': 80_000,
    'full-time': False
}

print(employee2)
print(employee2['name'])

employee2['salary'] += 10000

print(employee2)

employee2.update({'age': 40})

print(employee2)

employee2['full-time'] = True

print(employee2)

print('-----------------------------------')

employee3 = {
    'name': 'Shay',
    'age': 29,
    'salary': 110_000,
    'full_time': False,
    'job_title': 'Developer',
    'company_name': 'Apple inc'
}

print(list(employee3.keys()))

for key in employee3.keys():
    print(key)

for key in employee3.keys():
    print(f'{key} : {employee3[key]}')

print('----------------------')
print(employee3.values())

values = list(employee3.values())

for values in employee3.values():
    print(values)

print('----------------------')

for x in employee3.items():
    print(x)

for x in employee3.items():
    print(f'{x[0]} : {x[1]}')

print('----------------------')

employees = {
    'E1': {
        'name': 'Shay',
        'age': 29,
        'salary': 110_000,
        'full_time': False,
        'job_title': 'Developer',
        'company_name': 'Apple inc'
    },
    'E2': {
        'name': 'Daniel',
        'age': 39,
        'salary': 90_000,
        'full_time': True,
        'job_title': 'Analyst',
        'company_name': 'Apple inc'
    },
    'E3': {
        'name': 'Yulia',
        'age': 26,
        'salary': 115_000,
        'full_time': True,
        'job_title': 'QA',
        'company_name': 'Google inc'
    }
}

print(employees)

print('----------------------')

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

students['S1']['gpa'] = 2.5
students['S2'].update({'name': 'Daniel', 'gender': 'Male'})

print(students)

students['S2']['name'] = 'Georgina'
students['S2']['gender'] = 'Female'

print(students)

students['S3']['subject'][1] = 'Biology'
students['S3']['subject'].append('Programming')

print(students)

print('----------------------')


for x in students.items():
    print(x)

print('----------------------')

for x in students.items():
    print(x[1])

print('----------------------')

for x in students.items():
    # print(x[1])
    for y in x:
        print(y)
print('----------------------')
print('----------------------')
print('----------------------')


for value in students.values():
    print(value)
    for item in value.items():
        print(item[1])
