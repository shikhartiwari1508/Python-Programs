x= int(input("Enter the number:-"))
match x:
    case 0:
        print(" x is zero")
    case 5:
        print (" x is 5")
    case _:
        print("The value of 'x' is :", x)
        