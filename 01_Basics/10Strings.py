chai = "Lemon chai"
print(chai)

chai = "Masala chai"

first_char = chai[0]
print(first_char)

slice_chai = chai[0:6]
print(slice_chai)
print(chai[-1])

num_list = "0123456789"

num_slice = num_list[:]
print(num_slice)

num_slice = num_list[3:]
print(num_slice)

num_slice = num_list[:7]
print(num_slice)

num_slice = num_list[0:7:2]
print(num_slice)

num_slice = num_list[0:7:3]
print(num_slice)

chai  = "Masala Chai"
print(chai.lower())
print(chai.upper())

chai  = "   Masala Chai  "
print(chai)
print(chai.strip())

chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))
print(chai)

chai  = "Lemon , Ginger, Masala, Mint"
print(chai.split(", "))

chai  = "Masala Chai"
print(chai.find("Chai"))
print(chai.find("Chai"))

chai = "Masala Chai Chai chai"
print(chai.count("Chai"))

chai_type = "Masala Chai"
quantity = 2
order = "I ordered {} cupps of {} chai"
print(order.format(quantity, chai_type))

chai_variety = ["Lemon", "Masala", "Ginger"]
print(chai_variety)
print(", ".join(chai_variety))

chai = "Masala Chai"
print(len(chai))

for letter in chai:
    print(letter) 

chai = "He said, \"Masala chai is awesome\" "
print(chai)

chai = "Masala\nChai"
print(chai)

chai = r"Masala\nChai"
print(chai)

chai = r"c:\\user\\pwd\\"
print(chai)

chai = r"c:\\user\\pwd"
print(chai)

chai = "c:\\user\\pwd"
print(chai)

chai = "Masala Chai"
print("Masala" in chai)
print("Masaala" in chai)