class Employee:
    def __init__(self, __name: str, __salary: float):
        self.__name = __name
        self.__salary = __salary

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary: float):
        if new_salary <= self.__salary:
            print('the amount is less than the previous one')
        elif new_salary > self.__salary:
            self.__salary = new_salary
            print(f'new salary: {self.__salary}', self.__salary)

    def __str__(self):
        return f'Name: {self.__name}, salary: {self.__salary}'


class Manager(Employee):
    def __init__(self, __name: str, __salary: float, bonus: float):
        super().__init__(__name, __salary)
        self.bonus = bonus

    def override_salary_property(self):
        return self.salary + self.bonus

class Department:
    def __init__(self, employees: list=None):
        self.employees = employees
        if employees is None:
            self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f'add employee {employee.name}, salary: {employee.salary}')

    def total_payroll(self):
        total = 0
        for employee in self.employees:
            total += employee.salary
        print(f'total payroll: {total}')
        return total


# Output

employee1 = Employee('Itadori Yuji', 1700)
print(employee1)

employee2 = Employee('Gojo Satoru', 2300)
print(employee2)

print(employee1.name, employee1.salary)
print(employee2.name, employee2.salary)

manager = Manager('toji fushiguro', 1800, 300)
print(manager)

department = Department()

department.add_employee(employee1)
department.add_employee(employee2)
department.add_employee(manager)

department.total_payroll()