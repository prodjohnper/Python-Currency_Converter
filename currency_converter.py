# Currency converter

import requests

API_KEY = 'fca_live_xskSf5VEoCRq6pgd4N8idoh9F1Z5Rnb4iqc8Eq85'
URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
ON = True

CURRENCIES = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'MXN']

print('\nWelcome to Currency Converter!\n')

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
        print('Invalid selection, try again.')
        print("Type 'Exit' to exit program.")
        return None
    
def prog_help():
    print('\nCurrency converter user manual.\n')
    print('To use the program, enter the desired currency.')
    print('You can also select the conversion amount by typing it after the currency.')
    print('Example: USD 100.\n')
    print('Available currencies: AUD, EUR, GBP, JPY, MXN, USD.\n')
    print("Typing 'Currencies' displays the available currencies for conversion.")
    print("Typing 'Help' displays the program manual page.")
    print("Type 'Exit' to exit the program.")
    return ''

def available_currencies():
    print('Available currencies: AUD, EUR, GBP, JPY, MXN, USD.')
    return ''

while ON:
    user_input = input("Enter currency (Type 'Help' for user manual or 'Exit' to quit): ").upper()
    if user_input == 'EXIT':
        print('\nThanks for using Currency Converter! Closing program...\n')
        break
    elif user_input == 'HELP':
        print(prog_help())
        continue
    elif user_input == 'CURRENCIES':
        print(available_currencies())
        continue

    try:
        base, * amount_str = user_input.split()
        amount = float(amount_str[0]) if amount_str else None
    except ValueError:
        print('Invalid input format, try again.')
        print("Type 'Exit' to exit program\n.")
        continue

    if base not in CURRENCIES:
        print('\nInvalid selection, try again.')
        print("Type 'Exit' to exit program.\n")
        continue

    data = currency_converter(base, amount)
    if not data:
        continue

    for ticker, value in data.items():
        print(f'{ticker}: {value}')

    print("\nType 'Exit' to exit program.\n")

# Jonathan Perez - @prodjohnper - jonathanperez9743@gmail.com
