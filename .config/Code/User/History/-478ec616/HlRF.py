devices = []

file = ("devices.txt", "r")

for item in file:
    item = item.strip()
    devices.append(item)
print(devices)