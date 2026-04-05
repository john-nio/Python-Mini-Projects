def start_convertor():
    print("Welcome to currency Converter")
    currencies = {"1": "USD", "2": "CAD", "3": "Euro"}

    while True:
        source_choice = input(
            "Select Source Currency (1. USD, 2. CAD, 3. Euro, q to quit): "
        ).lower()
        if source_choice == "q":
            print("Thanks for using the converter!")
            break

        target_choice = input(
            "Select Target Currency (1. USD, 2. CAD, 3. Euro, q to quit): "
        ).lower()
        if target_choice == "q":
            print("Thanks for using the converter!")
            break

        if source_choice in currencies and target_choice in currencies:
            currency_exchange(currencies[source_choice], currencies[target_choice])
        else:
            print("Invalid Choice. Try Again.\n")


def currency_exchange(source, target):
    # Hardcoded exchange rates relative to USD for this example
    exchange_rates = {"USD": 1.0, "CAD": 1.35, "Euro": 0.92}

    try:
        source_value = float(input(f"Enter the {source} value you want to convert: "))
        # Convert source to USD first, then to target currency
        usd_value = source_value / exchange_rates[source]
        target_value = usd_value * exchange_rates[target]

        print(
            f"{source_value:.2f} {source} is equivalent to {target_value:.2f} {target}\n"
        )
    except ValueError:
        print("Invalid Value. Please enter a numerical value.\n")


if __name__ == "__main__":
    start_convertor()
