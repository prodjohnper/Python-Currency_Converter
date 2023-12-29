# Currency converter

import requests

API_KEY = 'fca_live_xskSf5VEoCRq6pgd4N8idoh9F1Z5Rnb4iqc8Eq85'
URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
ON = True

CURRENCIES = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'MXN']

def currency_converter(base, amount=None):
    currencies = ','.join(CURRENCIES)
    url = f'{URL}&base_currency={base}&currencies={currencies}'
    try:
        response = requests.get(url)
        data = response.json()['data']
        if amount is not None:
            return {ticker: value * amount for ticker, value in data.items() if ticker != base}
        else:
            del data[base]
            return data
    except:
        print('Invalid currency selection, try again.')
        print("Type 'Exit' to exit program")
        return None

while ON:
    user_input = input('\nEnter currency: ').upper()
    if user_input == 'EXIT':
        break

    try:
        base, *amount_str = user_input.split()
        amount = float(amount_str[0]) if amount_str else None
    except ValueError:
        print('Invalid input format, try again.')
        print("Type 'Exit' to exit program")
        continue

    if base not in CURRENCIES:
        print('Invalid selection, try again.')
        print("Type 'Exit' to exit program")
        continue

    data = currency_converter(base, amount)
    if not data:
        continue

    for ticker, value in data.items():
        print(f'{ticker}: {value}')

    print("\nType 'Exit' to exit program")

# Jonathan Perez - @prodjohnper
