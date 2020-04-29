import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def preform_math():
    global run
    global previous
    equation = ""
    if previous is 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Goodbye, Human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous is 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    preform_math()