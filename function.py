#Function creation:

def greet():
    print("Hello Students....")
greet()    

#with parameter:

def add(a,b):
    print(a + b)
add(10,20)    

#Return statement:

def square(n):
    return n * n
result = square(5)
print(result)

#Lambda function:

squrae = lambda x : x * x
print(square(4))

#Recursive function:

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))