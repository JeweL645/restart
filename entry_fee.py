#Dream Holiday Park

age = int(input("Enter your age: "))

if age < 4:
    price = 0

elif age >= 65:
    price = 10

else:
    price = 5
print("Your admission fee is "+ str(price) + "$")
print("Enjoy your time!!")
