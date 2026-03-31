email = "aa@gmail.com"
password = "12sfgsgs"
password = password.strip()

if password == "":
    print("Password must not be empty")
elif len(password) <= 7:
    print("Password must be atleast 8 characters")
elif password == email:
    print("Password and email cannot be same")
elif not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")
elif password.islower() or password.isupper():
    print("Password must include at least 1 uppercase and 1 lowercase letter")
else:
    print("Password is valid")
