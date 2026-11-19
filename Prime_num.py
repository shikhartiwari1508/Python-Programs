# Program to check Prime Number

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
