import datetime
def get_days_from_today(date_str):
    try:
        input_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        today_date = datetime.date.today()
        delta = input_date - today_date
        return delta.days
    except ValueError:
        return "Введена дата має неправильний формат. Будь ласка, введіть дату у форматі 'РРРР-ММ-ДД'."

result = get_days_from_today("2021-10-09")
print(result)
