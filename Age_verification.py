age = int(input("Enter your age: "))
if age >= 18:
    print("Access granted.")
else:
    print(f"Access denied. Try again in {18 - age} years.")