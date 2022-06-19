import re

def change_date_format(date_old):
    pattern = re.compile(r'([0-9]{2}).([0-9]{2}).([0-9]{4})')
    res = pattern.search(date_old)
    day = res.group(1)
    month = res.group(2)
    year = res.group(3)
    return f'{year} {month} {day}'

print(change_date_format('21.11.2223'))