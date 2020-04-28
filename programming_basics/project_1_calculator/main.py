import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def preform_math():
    global run
    global previous
    equation = input("Enter equation:")
    if equation == 'quit':
        run = False
    else:
        previous = equation
        print("You typed", previous)

while run:
    preform_math()