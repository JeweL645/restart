
while True:
    alien_color = input("Enter the color of the alien: ")

    if alien_color == 'green':
        print("You have earned 5 points!")
    elif alien_color == 'yellow':
        print("You have earned 10 points!")
    elif alien_color == 'red':
        print("You have earned 15 points!")

    print()
    c = input('Do you want to continue the program? \nY/N: ')

    if c.lower() == 'y':
        break

