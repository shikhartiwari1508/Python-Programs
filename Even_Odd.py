num = int(input("Enter the number ="))
if(num % 2 == 0):
    print("Even Number")
else:
    print("Odd number")    


# Print all even numbers from 1 to n

num = int(input("Enter the Numbers : "))
for i in range (1, num +1):
    if i % 2 == 0:
        print(i,end =" ")


# Print all odd numbers from 1 to n

num = int(input("Enter the Numbers : "))
for i in range (1, num +1):
    if i % 2 != 0:
        print(i,end =" ")
