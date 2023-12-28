# *Currency Converter*

### Table of contents

- [Description](#description)
- [Files](#files)
- [Features](#features)
- [Usage](#usage)
- [Credits](#credits)

## Description

This is a simple *currency converter* made using *[FreecurrencyAPI's](https://app.freecurrencyapi.com/)* currency converter *API*. You can do simple currency conversions by typing the desired currency to be exchanged and the program runs the conversions and returns an output containing multiple conversions to other currencies. Further support for bigger conversions is being worked at the moment as it only works with single unit conversions for the time being.

## Files

- `AUTHORS` - File that contains the project authors.
- `README.md` - File that contains project description.
- `currency_converter.py` - Main function.

## Features

This are the currencie conversions this program can run:

- `USD` - United States of America dollar conversion.
- `EUR` - European Euro conversion.
- `JPY` - Japanese Yen conversion.
- `GBP` - British Pound Sterling conversion.
- `AUD` - Australian Dollar conversion. 
- `MXN` - Mexican Peso conversion.
- `Exit`- Exits the program.

## Usage

To use the program, run the `python currency_converter.py` command on your terminal:

```c
prodjohnper@penguin:~/Python-Currency_converter$ python currency_converter.py
```

Then type the desired currency to execute the conversion:

```c
prodjohnper@penguin:~/Python-Currency_converter$ python currency_converter.py

Enter currency: USD
AUD: 1.4591801604
EUR: 0.9001801523
GBP: 0.781330149
JPY: 141.4057920549
MXN: 16.9212520451

Type 'Exit' to exit program

Enter currency:
```

When done, close the program typing `Exit`:

```c
prodjohnper@penguin:~/Python-Currency_converter$ python currency_converter.py

Enter currency: USD
AUD: 1.4591801604
EUR: 0.9001801523
GBP: 0.781330149
JPY: 141.4057920549
MXN: 16.9212520451

Type 'Exit' to exit program

Enter currency: Exit
prodjohnper@penguin:~/Python-Currency_converter$
```

## Credits

- *[Jonathan Pérez](https://github.com/prodjohnper)*
