class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):
    def __init__(self, name: str, age: int, job_title: str, company_name: str = 'unknown', salary: int = 0):
        super().__init__(name, age)
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')


class Developer(Employee):
    def __init__(self, name: str, age: int, job_title: str = 'Software Developer', company_name: str = 'unknown', salary: int = 0):
        super().__init__(name, age, job_title, company_name, salary)


employee_1 = Employee('Hazel', 27, 'QA', 'Apple inc')
developer_1 = Developer('Daniel', 35, 'Python Developer', 'Google inc',150000)

print(employee_1)
print(developer_1)
