import re

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 asf  "
]

for phone in phone_numbers:
    # cleaned_number = re.sub(r'\D', '', phone)
    cleaned_number = re.sub(r'[^0-9]', '', phone)
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    print(cleaned_number)