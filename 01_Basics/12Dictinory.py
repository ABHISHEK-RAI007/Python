chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)

print(chai_types["Masala"])

print(chai_types.get("Ginger"))

chai_types["Green"] = "Fresh"
print(chai_types)

for chai in chai_types:
    print(chai)

for chai in chai_types:
    print(chai, chai_types[chai])

for (key, value) in chai_types.items():
    print(key, value)

if "Masala" in chai_types:
    print("I have Masala Chai")

print(len(chai_types))

chai_types["Earl Grey"] = "Citrus"
print(chai_types)

x = chai_types.pop("Ginger")
print(chai_types)

y = chai_types.popitem()
print(y)

print(chai_types)

del chai_types["Green"]
print(chai_types)

chai_type_copy = chai_types.copy()

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea" : {"Green": "Mild", "Black": "Strong"}
}
print(tea_shop)

a =tea_shop["chai"]["Ginger"]
print(a)

squared_num = {x:x**2 for x in range(0,6)}
print(squared_num)
squared_num.clear()
print(squared_num)

keys = ["Masala", "Ginger", "Lemon"]
print(keys)
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

new_dict = dict.fromkeys(keys, keys)
print(new_dict)