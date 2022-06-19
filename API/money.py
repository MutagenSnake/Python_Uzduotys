import requests
import json

# site = requests.get("https://api.frankfurter.app/latest")
# dictionary = json.loads(site.text)
# base_currency = dictionary['base']
# base_rate_to_USD = dictionary['rates']['USD']
# print(f'{base_currency} to USD: {base_rate_to_USD}')



# site = requests.get("https://api.frankfurter.app/latest?to=USD,GBP")
# dictionary = json.loads(site.text)
# print(dictionary)

# site = requests.get("https://api.frankfurter.app/latest?from=USD")
# dictionary = json.loads(site.text)
# print(dictionary)

def get_rate(base,target):
    try:
        site = requests.get(f"https://api.frankfurter.app/latest?from={base}")
        dictionary = json.loads(site.text)
        base_rate_to_target = dictionary['rates'][f'{target}']
        print(f'{base} to {target}: {base_rate_to_target}')
    except Exception:
        print('Blogai suvestos valiutos')
        site = requests.get("https://api.frankfurter.app/latest")
        dictionary = json.loads(site.text)
        second_dict = dictionary['rates']
        list_of_currencies = []
        list_of_currencies.append(dictionary['base'])
        rest_of_currencies = second_dict.keys()
        for currency in rest_of_currencies:
            list_of_currencies.append(currency)
        print('available currencies:')
        for currency in list_of_currencies:
            print(currency)


get_rate('DKK', 'BBB')