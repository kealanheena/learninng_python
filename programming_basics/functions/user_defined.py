
# ADDING ARGUMENTS
# def my_function(str1, str2):
#     print(str1)
#     print(str2)

# my_function("Hello", "World")
# my_function("Str one", "Str two")

# DEFAULT ARGUMENTS
# def print_something(name = "Someone", age = "Unknown"):
#     print("My name is ", name, "and my age is", age)

# print_something("Nick")

# KEYWORD ARGUMENTS
# def print_something(name = "Someone", age = "Unknown"):
#     print("My name is ", name, "and my age is", age)

# print_something(age = 27)

# INFINATE ARGUMENTS
# def print_people(*people):
#     for person in  people:
#         print("This person is", person)
    
# print_people("Nick", "Mark", "Jack", "Jon")

# RETURN VALUES FROM FUNCTION
def do_math(num1, num2):
    return num1 + num2

math1 = do_math(5, 7)
math2 = do_math(11, 34)

print("First sum is", math1, "and second sum is", math2)
