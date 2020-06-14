
while True:
    age = int(input("Enter your age :"))

    if age < 2:
        print("You are a baby! ")
    elif age >= 2 and age < 4:
        print("You are a toddler! ")
    elif age >= 4 and age < 13:
        print("You are a kiddo! ")
    elif age >= 13 and age < 20:
        print("You are a teenager! ")
    elif age >= 20 and age < 65:
        print("You are an adult! ")
    elif age >= 65:
        print("You are an elder!\n")

    choice = input("Do you want to continue the program?\nY/N: ")
    if choice.lower() == 'n':
        break

