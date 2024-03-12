import emoji
name = input("Enter your friend name: ")

def greeting(name):
    return ("Hello, " + name + "! " + emoji.emojize("😍"))

print(greeting(name))
