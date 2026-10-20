# Files ko unke extensions ke basis par alag folders mein organize karega.



import os
import shutil

folder = input("Enter folder path: ")

categories = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

for filename in os.listdir(folder):
    source = os.path.join(folder, filename)

    if not os.path.isfile(source):
        continue

    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in categories.items():
        if extension in extensions:
            target_folder = os.path.join(folder, category)
            os.makedirs(target_folder, exist_ok=True)

            destination = os.path.join(target_folder, filename)

            if not os.path.exists(destination):
                shutil.move(source, destination)
                print(filename, "moved to", category)

            break
