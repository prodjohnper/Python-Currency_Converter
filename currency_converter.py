# Currency converter

import requests

API_KEY = 'fca_live_xskSf5VEoCRq6pgd4N8idoh9F1Z5Rnb4iqc8Eq85'
URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
ON = True

CURRENCIES = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'MXN']

def currency_converter(base):
    currencies = ','.join(CURRENCIES)
    url = f'{URL}&base_currency={base}&currencies={currencies}'
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except:
        print('Invalid currency selection, try again.')
        print("Type 'Exit' to exit program")
        return None

while ON:
    base = input('\nEnter currency: ').upper()
    if base == 'EXIT':
        break
    if base not in CURRENCIES:
            print('Invalid currency selection, try again.')
            print("Type 'Exit' to exit program")
            continue
    
    data = currency_converter(base)
    if not data:
        continue
    del data[base]
    
    for ticker, value in data.items():
        print(f'{ticker}: {value}')
    print("\nType 'Exit' to exit program")

# Jonathan Perez - @prodjohnper
