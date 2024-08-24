"""specify the number of Bitcoins as a command-line argument ,
Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator."""

import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        amount = float(sys.argv[1])

        price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        usd = float(price.json()["bpi"]["USD"]["rate"].replace(',', ''))

        print(f"${(amount * usd):,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")

except requests.RequestException:
    sys.exit("...")
