'''a=int(input("Enter the first number="))
b=int(input("Enter the second number="))


print("Addition")
Addition=print( a+b)


print("Subtraction")
Subtraction=print( a-b)


print("Multiplication")
Multiplication=print( a*b)


print("Division")
Division=print( a/b)'''


#using function

def numbers(num1 , num2 ):
    sum = num1 + num2
    sub = num1 - num2 
    mult = num1 * num2
    div = num1 / num2
    print ("sum :",sum)
    print ("sub :",sub)
    print ("mult :",mult)
    print ("div :",div)
numbers(10,5)    
