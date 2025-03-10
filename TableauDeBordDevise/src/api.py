from datetime import date, timedelta
from pprint import pprint

import requests

def get_rates(currencies, days=30):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symbols = ','.join(currencies)
    url = f"https://www.docstring.fr/api/rates/history/?start_at={start_date}&end_at={end_date}&symbols={symbols}"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Error get: {r.status_code}")
        return None

    api_rates = r.json().get('rates')
    if api_rates is None:
        print("Error: No data received from API")
        return None
    all_rates = {currency: [] for currency in currencies}

    all_days = sorted(api_rates.keys())
    pprint(f"Data loaded for {len(all_days)} days")

    for day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[day].items()]

    return all_days, all_rates

if __name__ == '__main__':
    days, rates = get_rates(currencies=["USD", "EUR"])

    pprint(days)
    pprint(rates)

    if rates is None:
        print("Error fetching data from the API.")
    print("Loading data from the API")