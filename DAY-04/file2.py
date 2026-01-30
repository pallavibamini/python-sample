#create a csv file 
# file=open("data.csv","w")
# file.write("Name,Age,City\n")
# file.write("Alice,30,New York\n")
# file.write("Bob,25,Los Angeles\n")
# file.write("Charlie,35,Chicago\n")
# file.close()
# file=open("data.csv","r")
# content=file.read() 
# print(content)

# file=open("sample_log.log","w")
# file.close()


# file=open("sample_log.log","r")
# content=file.read() 
# print(content) 

ip_addresses = []

with open("sample_log.log", "r") as log:
    lines = log.readlines()
    for line in lines:
        if "abc" in line:
            words = line.split("[")
            ip_addr = words[1].strip("]\n")
            ip_addresses.append(ip_addr[0])

with open("ip_addresses.txt", "w") as ip:
    for addr in ip_addresses:
        ip.write(addr + "\n")

print("successful")



