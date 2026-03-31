def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100


orders = [100, 200, 300]

for price in orders:
    final_amount = price + add_vat(price, 10)
    print(f"Orginal Value: {price}, After VAT {final_amount}")
