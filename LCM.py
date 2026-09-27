a = int (input("Enter the first number : "))
b = int (input("Enter the Second number : "))
lcm = max(a,b)
while True :
    if lcm % a == 0 and lcm % b == 0 :
        break
    lcm = lcm + 1
print("LCM = ", lcm)    