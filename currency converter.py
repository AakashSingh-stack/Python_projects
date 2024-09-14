import urllib.request

def fetch_exchange_rates():
    try:
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        with urllib.request.urlopen(url) as response:
            exchange_rates_data = response.read()
            exchange_rates_data = exchange_rates_data.decode('utf-8')
            return eval(exchange_rates_data)['rates']
    except urllib.error.URLError as e:
        print("Error fetching exchange rates:", e)
        return None

def convert_currency(amount, source_currency, target_currency, exchange_rates):
    try:
        source_rate = exchange_rates[source_currency.upper()]
        target_rate = exchange_rates[target_currency.upper()]
        converted_amount = amount / source_rate * target_rate
        return round(converted_amount, 2)
    except KeyError:
        print("Invalid currency code.")
        return None

def main():
    print("Welcome to the Currency Converter!")

    exchange_rates = fetch_exchange_rates()

    if exchange_rates is None:
        return

    while True:
        try:
            amount = float(input("Enter the amount: "))
            source_currency = input("Enter the source currency code (e.g., USD): ").upper()
            target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

            converted_amount = convert_currency(amount, source_currency, target_currency, exchange_rates)

            if converted_amount is not None:
                print(f"{amount} {source_currency} is equal to {converted_amount} {target_currency}.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
