import re

try:
    with open('mbox.txt', 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File 'mbox.txt' not found.")
    exit()

pattern = r'^From:\s+.*@(\S+)'

host_set = set()

for line in lines:
    if line.startswith("From:"):
        match = re.search(pattern, line)
        if match:
            host = match.group(1)
            host_set.add(host)
            print(host)

print(f"Total {len(host_set)} hosts printed")
