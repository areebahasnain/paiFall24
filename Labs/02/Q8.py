def currency_converter():
    # Exchange rates relative to 1 USD
    rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'PKR': 296.0,
        'INR': 83.0,
        'YEN': 145.0
    }
    
    # Available currencies
    currencies = ['USD', 'EUR', 'PKR', 'INR', 'YEN']

    # Input currency to convert from
    from_currency = input("Enter the currency you want to convert from (USD, EUR, PKR, INR, YEN): ").upper() # upper() to convert to uppercase
    if from_currency not in currencies:
        print("Invalid currency. Please try again.")
        return

    # Input amount to convert
    amount = float(input(f"Enter the amount in {from_currency}: "))

    # Input currency to convert to
    to_currency = input("Enter the currency you want to convert to (USD, EUR, PKR, INR, YEN): ").upper()
    if to_currency not in currencies:
        print("Invalid currency. Please try again.")
        return

    # Conversion process
    if from_currency == to_currency:
        converted_amount = amount
    else:
        # Convert the amount to USD first, then to the desired currency
        amount_in_usd = amount / rates[from_currency]
        converted_amount = amount_in_usd * rates[to_currency]

    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")

# Run the currency converter
currency_converter()
