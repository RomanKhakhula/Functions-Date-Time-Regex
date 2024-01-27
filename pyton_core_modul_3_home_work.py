import datetime, re, random
from datetime import datetime, date, timedelta

# Task 1: Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
def get_days_from_today(str_d: str) -> int:
    """Arg.: string 'YYYY-MM-DD'. Return difference between inputed date and current date in days."""
    if re.search(r"\d{4}-\d{2}-\d{2}", str_d):
        return print(datetime.today().date().toordinal() - datetime.strptime(str_d, "%Y-%m-%d").date().toordinal())
    else:
        return print("Incorrect date format, expected -> 'YYYY-MM-DD'! Please check out and try again!")

# Task 1 check:
# get_days_from_today('2023-01-23')
# get_days_from_today('23-01-01')
# str_d = input("Please input date in following format 'YYYY-MM-DD'': ")
# get_days_from_today(str_d)

# Task 2: Необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
def get_numbers_ticket(a = -1, b = -1, c = -1):
    """Arg.: a, b, c -> int, a >= 1, a < b <= 1000, a <= c <= b. Return sorted list of c unique numbers from range a - b."""
    try:
        if a >= 1 and (a < b <= 1000) and (a <= c <= b):
            list_of_numbers = []
            for i in range(a, b + 1):
                list_of_numbers.append(i)
            return f"Lottery numbers: {sorted(random.sample(list_of_numbers, c))}"
        else:
            return []
    except Exception:
        return []         

# Task 2 check:
# print(get_numbers_ticket(1,20,10))
# print(get_numbers_ticket())
# print(get_numbers_ticket('a','b','c'))

# Task 3: Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку
def normalize_phone(phone_number):
    """Arg.: str (phone number). Return normalized str (phone number): '+380XXXXXXXXX' """
    a = re.findall(r"[\d*]", phone_number)
    b = ''
    for el in a:
        b += el
    return "+380" + b[-9::]

# Task 3 check:
# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# print(raw_numbers) 
# normalized_number = [normalize_phone(el) for el in raw_numbers]
# print(normalized_number) 

# Task 4:  Потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати
def get_upcoming_birthdays(users):
    """Arg.: list of dicts with user name and user birthday. Return list of dicts with user name and congratulation date"""
    upcoming_birthdays = []
    for el in users:
        this_year_bd = datetime.strptime(re.sub(r"\d{4}", datetime.strftime(datetime.now().date(), "%Y"), el["birthday"]), "%Y.%m.%d").date()
        if 0 <= (this_year_bd - datetime.now().date()).days <= 7:
            if this_year_bd.isoweekday() == 6: 
                congratulation_date = this_year_bd + timedelta(days=2) 
            elif this_year_bd.isoweekday() == 7:
                congratulation_date = this_year_bd + timedelta(days=1)
            else:
                congratulation_date = this_year_bd
            upcoming_birthdays.append({"name": el["name"], "congratulation_date": datetime.strftime(congratulation_date, "%Y.%m.%d")})
        else: 
            continue
    return upcoming_birthdays


# Task 3 check:
# users = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}
# ]

# print(get_upcoming_birthdays(users))