while True:
    for i in range(0, 3):
        agree = input("Do you agree? ")
        if agree == "yes":
            print("Glad you are on the same page")
            break
    else:
        print("3 strikes, you are out")
