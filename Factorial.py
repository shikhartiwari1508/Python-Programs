'''num = int(input("Enter the number = "))
factorial = 1
if num < 0:
    print("Sorry, factorial doesn't exist zero")
elif num == 0:
    print("the factorial of 0 is 1")
else :
    for i in range (1, num + 1):
        factorial = factorial*i
    print("The factoril of" , num, "is :",factorial)'''       


# OR

x= int(input("Enter the number = "))
def factorial(x):
    if(x==0) or (x==1):
        return 1
    else:
        return x*factorial(x-1)
print(factorial(x))
