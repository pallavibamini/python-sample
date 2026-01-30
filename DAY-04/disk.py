#disk usage monitoring script(ram,cpu) how much memory used , how much free memory available, total memory
# import psutil
# def display_disk_usage():
#     disk_usage = psutil.disk_usage('/')
#     print("Disk Usage Information:")
#     print(f"Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
#     print(f"Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
#     print(f"Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")
#     print(f"Disk Usage Percentage: {disk_usage.percent}%")

# display_disk_usage()

import shutil
def display_disk_usage():
    total, used, free = shutil.disk_usage("/")
    bytes=1024**3
    print("Disk Usage Information:")
    print(f"Total Disk Space: {total / bytes} GB")
    print(f"Used Disk Space: {used / bytes} GB")
    print(f"Free Disk Space: {free / bytes} GB")
    print(f"Disk Usage Percentage: {(used / total) * 100}%")
display_disk_usage()

