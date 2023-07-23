
# Open the file
with open("DOB.txt", "r") as file:
    lines = file.readlines()

# Split the lines into names and birthdates
names = []
birthdates = []
for line in lines:
    values = line.strip().split(",")
    if len(values) == 2:
        names.append(values[0])
        birthdates.append(values[1])
    else:
        print(f"Ignoring line: {line}")

# Print the names section
print("Name")
for name in names:
    print(name)

# Print the birthdate section
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)
