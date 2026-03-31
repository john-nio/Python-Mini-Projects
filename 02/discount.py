users = [
    {"id": 1, "total": 120, "coupon": "P20"},
    {"id": 2, "total": 220, "coupon": "G20"},
    {"id": 3, "total": 340, "coupon": "L30"},
]

discounts = {"P20": (0.20, 0), "G20": (0, 20), "L30": (0, 10)}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(
        f"{user['id']} paid {user['total']} gets a discount of {discount} in next visit"
    )
