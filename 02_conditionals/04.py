fruit = "Banana"

color = input("Enter a color: ")

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
    else:
        print("There is no Information about this fruit")