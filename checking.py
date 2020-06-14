print("Let's play an interesting game")
i = 1
while i != 0 :
    x = int(input('Take a number in your mind: '))
    # print(x)
    x1 = int(input('Take the same number from Aladin: '))
    # print(x1)
    x2 = int(input('I am giving you: '))
    x3 = x2 // 2
    # print(x2)
    half = (x + x1 + x2) // 2
    # print(half)
    s = int(input('Aladin wants his amount back, what say? '))
    # print(s)
    if s == 1:
        half = half - x1
        print("Now you have only :", x3)
        i = int(input('Do you want to exit? '))