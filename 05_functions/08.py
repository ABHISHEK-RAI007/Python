def print_kwargs(**kwargs):
    for (key, valiue) in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name = "ShaktiMan", power = "lazer")
print_kwargs( power = "lazer", name = "ShaktiMan")
print_kwargs( power = "lazer", name = "ShaktiMan", enemy = "Dr. Jackaal")




