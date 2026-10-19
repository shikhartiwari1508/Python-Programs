#Random Choice Picker (Decision Maker)

import random

options = input("Enter choices separated by commas: ").split(",")
chosen = random.choice(options).strip()
print(f"The winner is: {chosen}")