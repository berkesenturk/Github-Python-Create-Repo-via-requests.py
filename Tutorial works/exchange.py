import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="


currency_type_sell = input("Which currency type do you wish to sell? : ")
currency_type_buy = input("Which currency type do you wish to buy? : ")
msell = int(input(f"How much {currency_type_sell} sell ?  : "))

result = requests.get(api_url+currency_type_sell)
result = json.loads(result.text)
print(result)
print("1 {0} = {1} {2}".format(currency_type_sell, result["rates"][currency_type_buy], currency_type_buy))
print("{0} {1} = {2}".format(msell, currency_type_sell, msell* result["rates"][currency_type_buy]))