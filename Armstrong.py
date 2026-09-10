num = int(input("Enter a number: "))

original = num
sum = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")