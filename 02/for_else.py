staff = [("Mani", 17), ("Sani", 22), ("Rani", 23)]
for name, age in staff:
    if age > 18:
        print(f"{name} eligible to vote")
    else:
        print(f"{name} is not eligible to vote")
