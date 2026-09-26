a = int(input("Enter the First Number : "))
b = int(input("enter the Second Number: "))
while b != 0:
    a,b = b , a%b
print("Greatest Common Divisor (GCD) : ",a)    
