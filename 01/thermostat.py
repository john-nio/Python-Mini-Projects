device_status = "off"
temperature = 25

if device_status == "active":
    if temperature > 35:
        print(f"It is hot!")
    else:
        print(f"Wait for some time")
else:
    print(f"Device is not active")
