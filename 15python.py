lines = []

while True:
    line = input("Enter a line (or leave blank to finish): ")
    if line == "":
        break  
    lines.append(line)

print("Lines entered:")
for line in lines:
    print(line)
