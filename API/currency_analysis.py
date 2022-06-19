# currency_pair_analysis('EUR', 'GBP', '2019-01-01', '2019-12-31')

import requests
import json

def currency_pair_analysis(from_date, to_date, base, target):
    # site = requests.get(f"https://api.frankfurter.app/{from_date}..{to_date}?from={base}?to={target}")
    site = requests.get(f"https://api.frankfurter.app/{from_date}..{to_date}?from={base}")
    dictionary = json.loads(site.text)
    new_dictionary = {}
    dictionary_rates = dictionary['rates']
    for key, value in dictionary_rates.items():
        new_dictionary[key] = value[target]
    max_value_date = max(new_dictionary, key=new_dictionary.get)
    min_value_date = min(new_dictionary, key=new_dictionary.get)

    print(f'Dates: {from_date} to {to_date}\n'
          f'Convesion: {base} to {target}\n'
          f'Maximum value was on {max_value_date}: {new_dictionary[max_value_date]}\n'
          f'Minimum value was on {min_value_date}: {new_dictionary[min_value_date]}')

currency_pair_analysis("2022-01-01", "2022-02-01","USD", "DKK")
