import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    content = response.json()
    price = content["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Network error")

print(f"${amount * price:,.4f}")