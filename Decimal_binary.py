num = int (input("Enter a decimal number : "))
binary = " "
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary 
    num = num // 2
print("Binary = ", binary)    