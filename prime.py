num = int(input("Enter the Number ="))
var = False
if num == 0 or num == 1:
    print(num , "is not a Prime Number")
elif num > 1:
    for i in range (2 , num):
        if (num % i) == 0:
            var = True
            break    
    if var:
        print (num , "is not a Prime Number")
    else:
        print(num , "is a Prime Number")     