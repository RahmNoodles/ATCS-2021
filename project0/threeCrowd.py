names = ["James", "Pranav", "Marco", "Zain"]

if len(names) > 3:
    print("The room is too crowded!")

names.remove("Marco")
names.remove("Pranav")
if len(names) > 3:
    print("The room is too crowded!")