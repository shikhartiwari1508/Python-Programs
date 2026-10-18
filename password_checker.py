#Simple Password Strength Checker
#Checks if a password is secure based on its length

password = input("Enter a password to check: ")
if len(password) >= 8:
    print("🔒 Strong password!")
else:
    print("⚠️ Weak password. Make it at least 8 characters.")