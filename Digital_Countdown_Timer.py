import time

seconds = 10
for remaining in range(seconds, 0, -1):
    print(f"⏳ Time remaining: {remaining} seconds", end="\r")
    time.sleep(1)
print("\n⏰ Time's up!")