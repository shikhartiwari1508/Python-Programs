n = int(input("Enter the Number : "))
i = 1
while i * i <= n:
    if i * i == n:
        print("Perfect Square ")
        break
    i = i+1
else:
    print("Not a Perfect Square")    
