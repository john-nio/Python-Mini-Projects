# The address should have a . and @


def address_validator(x):
    if "@" in x and "." in x:
        print("This is a valid email id")
        return True
    else:
        print(" A valid email id should have . and @")
        return False


while True:
    address = input("Type your mail id: ")
    if address_validator(address):
        break
