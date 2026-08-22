a=input("Enter the string :")
count = 0
for ch in a.lower():
    if ch in "aeiou":
        count +=1
print("Numbers of vowels = ", count)        