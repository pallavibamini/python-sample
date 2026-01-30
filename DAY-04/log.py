#log file analyzer
import os
import re
ip_addresses = []
with open("sample_log.log", "r") as log:
    lines = log.readlines()
    for line in lines:
        if re.search(r"ERROR", line):
            ip_addresses.append(line)
           
with open("error_logs.txt", "w") as error_file:
    for entry in ip_addresses:
        error_file.write(entry)
print("Error logs extracted successfully.") 





