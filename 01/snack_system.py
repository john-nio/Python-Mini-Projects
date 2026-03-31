snack = input("Enter your snack here: ").lower()
print(f"User said: {snack}")

if snack == "burger" or snack == "pizza":
    print(f"Great Choice! Your {snack} will be ready in 5 mins")
else:
    print(f"Sorry we dont have {snack}")
