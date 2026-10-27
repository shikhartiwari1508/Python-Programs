# User ka password check karega ki woh weak hai ya strong.



import re

password = input("Enter your password : ")

score = 0

if len(password) >= 8:
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[a-z]", password):
    score += 1
if re.search(r"[0-9]", password):
    score += 1
if re.search(r"[^A-Za-z0-9]", password):
    score += 1

if score <= 2:
    print("Password Strength:Your Password is Weak.")
elif score <= 4:
    print("Password Strength:Your Password is Medium.")
else:
    print("Password Strength:Your Password is Strong.")
