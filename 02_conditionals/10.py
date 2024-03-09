pet = input("What is your pet's species:")
pet_age = int(input("Enter your your pet's age:"))

if pet == "dog" and pet_age <= 2:
    print("AI recommends you Puppy food")
elif pet == "cat" and pet_age >= 5:
    print("AI recommends you Senior cat food")
else:
    print("There is no information available")