import datetime


def get_upcoming_birthdays(users: list) -> list:
    upcoming_birthdays = []
    today = datetime.date.today()
    for user in users:
        congratulation_date = None
        try:
            bornday = datetime.datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        except ValueError:
            print(f"User {user['name']} has invalid date format. Please use YYYY.MM.DD.")
            continue
        if bornday.month == 2 and bornday.day == 29 and not today.year % 4 == 0:
            continue
        birthday = datetime.date(today.year, bornday.month, bornday.day)
        if today <= birthday < today + datetime.timedelta(days=7):
            congratulation_date = birthday
        birthday = datetime.date(today.year + 1, bornday.month, bornday.day)
        if today <= birthday < today + datetime.timedelta(days=7):
            congratulation_date = birthday
        if congratulation_date is not None:
            if congratulation_date.weekday() in [5, 6]:
                congratulation_date += datetime.timedelta(days=7 - congratulation_date.weekday())
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': congratulation_date.strftime('%Y.%m.%d')})
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)