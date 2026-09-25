n = int(input("Enter the Number of terms = "))
a=0
b=1
for i in range(n):
    print(a, end = " ")
    a,b = b, a+b
