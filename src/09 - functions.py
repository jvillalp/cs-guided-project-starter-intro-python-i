"""
Functions
"""

# # 1. Defining a function
def my_function():
    print("Hello From My Function!")
my_function()
# # 2. Receiving arguments
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" %
          (username, greeting))

my_function_with_args("jvillalp", "hi!")

# # 3. Returning values
def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(2,2))

# # 4. Calling functions
# # Define our 3 functions
# def my_function():
#     print("Hello From My Function!")

# def my_function_with_args(username, greeting):
#     print("Hello, %s , From My Function!, I wish you %s" %
#           (username, greeting))

# def sum_two_numbers(a, b):
#     return a + b


# # print(a simple greeting)
# my_function()

# #prints - "Hello, John Doe, From My Function!, I wish you a great year!"
# my_function_with_args("John Doe", "a great year!")

# # after this line x will hold the value 3!
# x = sum_two_numbers(1, 2)