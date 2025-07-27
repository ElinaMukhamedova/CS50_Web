name = input("Name: ")
print(f"Hello, {name}")

n = int(input("Whole number: "))
if n > 0:
    print(f"{n} is positive")
elif n < 0:
    print(f"{n} is negative")
else:
    print(f"{n} is zero")

# Tuple
coordinates = (10.0, 20.0)

# List
names = ["Harry", "Ron", "Hermione", "Ginny"]
print(names[0])
names.append("Draco")
names.sort()
print(names)

# Set
s = set()
s.add(5)
s.add(3)
s.add(1)
s.add(3)
print(s)
s.remove(5)
print(s)

# Dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Hermione"] = "Gryffindor"
print(houses["Draco"])

# Loop
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

for i in range(6):
    print(i)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)