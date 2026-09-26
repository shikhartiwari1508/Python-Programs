text = input("Enter a String :")
count = 0
for char in text:
    if char.lower() in "aeiou":
        count = count + 1
print("Numbers of Vowel :", count)        