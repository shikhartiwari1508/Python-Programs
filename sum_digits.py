num = int(input("Enter the numbers :"))
sum = 0
while num > 0:
    digits = num % 10
    sum = sum + digits
    num = num // 10
print("Sum of Digits :", sum)    
