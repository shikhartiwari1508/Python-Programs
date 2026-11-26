# Program to check Palindrome String

text = input("Enter a string: ")

if text.lower() == text.lower()[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")
