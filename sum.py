# Sum of Even Numbers

num = int(input("Enter the Number : "))
sum = 0
for i in range(1, num + 1):
    if i % 2 == 0 :
        sum = sum + i
print("Sum of Even Numbers : ", sum) 


# Sum of Odd Numbers

num = int(input("Enter the Number : "))
sum = 0
for i in range(1, num + 1):
    if i % 2 != 0 :
        sum = sum + i
print("Sum of Odd Numbers : ", sum) 
