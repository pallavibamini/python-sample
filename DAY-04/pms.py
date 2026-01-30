#ping multiple servers script
import subprocess
servers = ["google.com", "yahoo.com", "bing.com", "github.com"]
for i in servers:
    response = subprocess.run(["ping", "-c", "1", i], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if response.returncode == 0:
        print(f"{i} is reachable.")
    else:
        print(f"{i} is not reachable.")