seat_type = input("Enter your seat type - Sleeper/AC: ").lower()

match seat_type:
    case "sleeper":
        print("No AC")
    case "ac":
        print("Comfy ride")
    case _:
        print("invalid seat type")
