a = input("Enter the string :- ")
if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")   




# OR

num = int(input("Enter the number :"))
original =num
reverse = 0
while num > 0:
    digit = num%10
    reverse = reverse * 10 + digit
    num = num // 10
if (original == reverse):
    print("Palindrome Number ") 
else:
    print("Not a Palindrome Number ")      