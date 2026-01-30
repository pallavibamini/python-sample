#folder clean up automation script
import os
folder_path=r"C:\Users\DELL\Desktop\project1\New folder"
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)
        print(f"Removed temporary file: {filename}")



