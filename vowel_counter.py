text = input("Enter text: ").lower()
vowels = sum(1 for char in text if char in "aeiou")
print(f"Total vowels: {vowels}")