from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.now().date()
        return (current_date - date).days
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


print(get_days_from_today("2021-10-09"))