# *Currency Converter*

### Table of contents

- [Description](#description)
- [Files](#files)
- [Features](#features)
- [Usage](#usage)
- [Credits](#credits)

## Description

This is a simple *currency converter* made using *[FreecurrencyAPI's](https://app.freecurrencyapi.com/)* currency converter *API*. You can do simple currency conversions by typing the desired currency, or typing the currency followed by the amount to be exchanged. The program thern runs the conversion and returns an output containing multiple conversions to other currencies. 

## Files

- `AUTHORS` - File that contains the project authors.
- `README.md` - File that contains project description.
- `currency_converter.py` - Main function.

## Features

This are the currency conversions this program can run:

- `USD` - United States Dollar conversion.
- `EUR` - European Euro conversion.
- `JPY` - Japanese Yen conversion.
- `GBP` - British Pound Sterling conversion.
- `AUD` - Australian Dollar conversion. 
- `MXN` - Mexican Peso conversion.
- `amount` - Program accepts currency amount input.
- `Currencies` - Displays available currencies.
- `Help` - Displays user manual.
- `Exit` - Exits/Closes the program.

## Usage

To use the program, run the `python currency_converter.py` command on your terminal:

```c
prodjohnper@penguin:~/Python-Currency_converter$ python currency_converter.py
```

Then type the desired currency to execute the conversion:

```c
prodjohnper@penguin:~/Python-Currency_converter$ python currency_converter.py

Enter currency (Type 'Help' for user manual or 'Exit' to quit): USD
AUD: 1.4591801604
EUR: 0.9001801523
GBP: 0.781330149
JPY: 141.4057920549
MXN: 16.9212520451

Type 'Exit' to exit program.

Enter currency (Type 'Help' for user manual or 'Exit' to quit):
```

It also works with an amount input:

```c
prodjohnper@penguin:~/Python-Currency_converter$ python currency_converter.py

Enter currency (Type 'Help' for user manual or 'Exit' to quit): USD 100
AUD: 146.47901939000002
EUR: 90.3350128
GBP: 78.53501547
JPY: 14141.64955992
MXN: 1696.09117251

Type 'Exit' to exit program.

Enter currency (Type 'Help' for user manual or 'Exit' to quit):
```

Typing `Currencies` displays the available currencies:

```c
prodjohnper@penguin:~/Python-Currency_converter$ python currency_converter.py

Enter currency (Type 'Help' for user manual or 'Exit' to quit): Currencies

Available currencies: AUD, EUR, GBP, JPY, MXN, USD.

Enter currency (Type 'Help' for user manual or 'Exit' to quit):
```

Typing `Help` displays the user manual:

```c
prodjohnper@penguin:~/Python-Currency_converter$ python currency_converter.py

Enter currency (Type 'Help' for user manual or 'Exit' to quit): Help

Currency converter user manual.

To use the program, enter the desired currency.
You can also select the conversion amount by typing it after the currency.       
Example: USD 100.

Available currencies: AUD, EUR, GBP, JPY, MXN, USD.

Type 'Help' displays the program manual page.
Type 'Exit' to exit the program.

Enter currency (Type 'Help' for user manual or 'Exit' to quit):
```

When done, close the program typing `Exit`:

```c
prodjohnper@penguin:~/Python-Currency_converter$ python currency_converter.py

Enter currency (Type 'Help' for user manual or 'Exit' to quit): USD
AUD: 1.4591801604
EUR: 0.9001801523
GBP: 0.781330149
JPY: 141.4057920549
MXN: 16.9212520451

Type 'Exit' to exit program.

Enter currency (Type 'Help' for user manual or 'Exit' to quit): Exit
prodjohnper@penguin:~/Python-Currency_converter$
```

## Credits

- *[Jonathan Pérez](https://github.com/prodjohnper)*
