x = 5*4*3*2*1

number = int(input("Enter a number: "))

factorial = 1

while number > 0:
    # factorial = factorial*number
    # number = number -1
    factorial *= number
    number -= 1

print("Factorial:", factorial)