"""
Создать базовый класс – работник, и производные классы – служащий с почасовой
оплатой, служащий в штате и служащий с процентной ставкой. Определить функцию
начисления зарплаты.
"""

class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError(" ")


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class CommissionEmployee(Employee):
    def __init__(self, name, sales_amount, commission_rate):
        super().__init__(name)
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def calculate_salary(self):
        return self.sales_amount * self.commission_rate

#сотрудники с разными типами оплаты труда
hourly_employee = HourlyEmployee(name="Mary", hourly_rate=20, hours_worked=400)
salaried_employee = SalariedEmployee(name="Ivan", monthly_salary=3000)
commission_employee = CommissionEmployee(name="Nikolay", sales_amount=50000, commission_rate=0.50)

#вывод зарплаты для каждого сотрудника
employees = [hourly_employee, salaried_employee, commission_employee]

for employee in employees:
    print(f"{employee.name} заработал(а): {employee.calculate_salary()} рублей")

