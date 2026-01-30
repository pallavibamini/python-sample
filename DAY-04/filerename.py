# file renamer script
import os
old_folder = "hello.txt"
new_folder = "greeting.txt"
os.rename(old_folder, new_folder)
print(f"Renamed '{old_folder}' to '{new_folder}'")


