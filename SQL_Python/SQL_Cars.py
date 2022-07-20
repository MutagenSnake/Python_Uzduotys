import sqlite3

def insert(manufacturer, model, color, year, price):
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()
    count = c.execute("select count(*) from cars")
    # list_total = list(count)
    # number = (list_total[0][0]) + 1
    with conn:
        c.execute("INSERT INTO cars VALUES(?,?,?,?,?)", (manufacturer, model, color, year, f'${price}'))

# insert('fake_manufacturer', 'audi', 'pink', '1919', 66969)

def search():
    base_string = 'SELECT * FROM cars WHERE year > 0 '
    search_string = ''
    parameter_input = input('Select parameters (1 - manufacturer, 2 - model, 3 - color, 4 - year, 5 - price(specific - skip))')
    if '1' in parameter_input:
        # manufacturer = input('Manufacturer: ')
        search_string += f"AND manufacturer='{input('Manufacturer: ')}' "
    if '2' in parameter_input:
        # manufacturer = input('Manufacturer: ')
        search_string += f"AND model='{input('Model: ')}' "
    if '3' in parameter_input:
        # manufacturer = input('Manufacturer: ')
        search_string += f"AND color='{input('Color: ')}' "
    if '4' in parameter_input:
        # manufacturer = input('Manufacturer: ')
        year_from = int(input('Year from: '))
        year_to = int(input('Year to: '))
        search_string += f"AND year > {year_from} AND year < {year_to} "
    if '5' in parameter_input:
        # manufacturer = input('Manufacturer: ')
        search_string += f"AND price='${input('Price: ')}' "
    conn = sqlite3.connect('cars.db')
    full_string = base_string + search_string
    print(full_string)
    c = conn.cursor()
    c.execute(full_string)
    res = c.fetchall()
    for item in res:
        print(item)

while True:
    what_to_do = int(input('Enter - 1, Search - 2, Done - 3:\n'))
    if what_to_do == 1:
        insert(input('Manufacturer:'), input('Model:'), input('Color:'), input('Year:'), int(input('Price:')))
    if what_to_do == 2:
        search()
    if what_to_do == 3:
        break