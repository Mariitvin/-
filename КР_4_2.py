'''
Создайте класс компания Company, содержащей сотрудников и реализующей методы:
•	найм одного сотрудника — hire(),
•	найм списка сотрудников – hireAll(),
•	увольнение сотрудника – fire(),
•	получение значения дохода компании – getIncome().
Аргументы и возвращаемое значение методов выберите на основании логики работы
вашего приложения.
2. Создайте два метода, возвращающие список указанной длины (count).
Они должны содержать сотрудников, отсортированных по убыванию и возрастанию
заработной платы:
•	List<Employee> getTopSalaryStaff(int count),
•	List<Employee> getLowestSalaryStaff(int count).
3. Создайте классы сотрудников с информацией о зарплатах и условиями начисления
зарплаты:
•	Manager — зарплата складывается из фиксированной части и бонуса в
виде 5% от заработанных для компании денег. Количество заработанных денег
для компании генерируйте случайным образом от 115 000 до 140 000 рублей.
•	TopManager — зарплата складывается из фиксированной части и бонуса
в виде 150% от заработной платы, если доход компании более 10 млн рублей.
•	Operator — зарплата складывается только из фиксированной части.
Каждый класс сотрудника должен  реализовывать метод, возвращающий зарплату
сотрудника:
•	getMonthSalary()
Аргументы и возвращаемое значение метода выберите в соответствии с логикой
начисления зарплат. 
'''
import random
class Employee:
    def get_month_salary(self):
        raise NotImplementedError

class Manager(Employee):
    def __init__(self, fixed_salary):
        self.fixed_salary = fixed_salary
        self.bonus = random.randint(115000, 140000) * 0.05
    def get_month_salary(self):
        return self.fixed_salary + self.bonus

class TopManager(Employee):
    def __init__(self, fixed_salary):
        self.fixed_salary = fixed_salary
    def get_month_salary(self, company_income):
        if company_income > 10_000_000:
            return self.fixed_salary * 2.5  #оклад + бонус
        else:
            return self.fixed_salary

class Operator(Employee):
    def __init__(self, fixed_salary):
        self.fixed_salary = fixed_salary
    def get_month_salary(self):
        return self.fixed_salary
    
class Company:
    def __init__(self):
        self.employees = []
        self.income = 0
    def hire(self, employee):
        self.employees.append(employee)
    def hire_all(self, employees):
        self.employees.extend(employees)
    def fire(self, employee):
        self.employees.remove(employee)
    def get_income(self):
        return self.income
    def set_income(self, income):
        self.income = income
    def get_top_salary_staff(self, count):
        return sorted(self.employees, key=self._get_employee_salary, reverse=True)[:count]
    def get_lowest_salary_staff(self, count):
        return sorted(self.employees, key=self._get_employee_salary)[:count]
    def _get_employee_salary(self, employee):
        if isinstance(employee, TopManager):
            return employee.get_month_salary(self.get_income())
        else:
            return employee.get_month_salary()

#cоздание компании
company = Company()
company.set_income(12_000_000)  #устанавливаем доход комании

#нанимаем сотрудников
manager = Manager(fixed_salary=30_000)
top_manager = TopManager(fixed_salary=80_000)
operator = Operator(fixed_salary=20_000)

company.hire(manager)
company.hire(top_manager)
company.hire(operator)

#список самых высокооплачиваемых сотрудников
top_salaries = company.get_top_salary_staff(2)
print("Список самых высокооплачиваемых сотрудников:")
for emp in top_salaries:
    if isinstance(emp, TopManager):
        print(type(emp).__name__, emp.get_month_salary(company.get_income()))
    else:
        print(type(emp).__name__, emp.get_month_salary())

#список самых низкооплачиваемых сотрудников
low_salaries = company.get_lowest_salary_staff(2)
print("\nСписок самых низкооплачиваемых сотрудников:")
for emp in low_salaries:
    if isinstance(emp, TopManager):
        print(type(emp).__name__, emp.get_month_salary(company.get_income()))
    else:
        print(type(emp).__name__, emp.get_month_salary())

