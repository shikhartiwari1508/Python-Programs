num = int(input("Enter the numbers :"))
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print("Number of Digits :", count)    