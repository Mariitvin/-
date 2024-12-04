import re
date_pattern = re.compile(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1[6-9][0-9]{2}|[2-9][0-9]{3})$")

def is_valid_date(date):
    match = date_pattern.match(date)
    if not match:
        return False

    day, month, year = map(int, date.split("/"))

    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29

    return 1 <= day <= days_in_month.get(month, 0)

valid_dates = ["29/02/2000", "30/04/2003", "01/01/2003"]
invalid_dates = ["29/02/2001", "30-04-2003", "1/1/1899"]

print("Проверка правильных дат:")
for date in valid_dates:
    print(f"{date}: {'Valid' if is_valid_date(date) else 'Invalid'}")

print("\nПроверка неправильных дат:")
for date in invalid_dates:
    print(f"{date}: {'Valid' if is_valid_date(date) else 'Invalid'}")
