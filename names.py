names = []

inp = ""

while inp != "q":
    inp = input("Name: ")
    if inp != "q":
        names.append(inp)
print(names)