tea_types = ("Black", "Green", "Oolong", )
print(tea_types)

x = tea_types[0]
print(x)

x = tea_types[-1]
print(x)

# tea_types[0] = "Lemon" # TypeError: 'tuple' object does not support item assignment
print(tea_types)

x = len(tea_types)
print(x)

more_tea = ("Herbal", "Earl Grey")
all_tea = tea_types + more_tea
print(all_tea)

if  "Green" in all_tea:
    print("Yes, Green Tea  is in the list")

more_tea = ("Herbal", "Earl Grey", "Herbal")
n = more_tea.count("Herbal")
print(n )

tea_types = ("Black", "Green", "Oolong")
(black, green, Oolong) = tea_types
print(black)


z = type(tea_types)
print(z)


