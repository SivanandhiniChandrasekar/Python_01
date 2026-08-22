# functions - a block of code that performs a specific task which improves code reusability...

# Why function - Code reusability, reduce code duplication, easy to understand

# Function Creation
def greet(stud_name):
    print("Hello "+stud_name+" !..")
# name = input()
# greet(name)
# greet(name)

# function definition - creating a function
# Function call - greet() --> calling a function

# Argument/ Parameters
# Argument - Actual value passed to the function.
# Paramter - Variable that receives the actual value i.e argument.

# Argument Types
# 1. Positional argument 
# 2. Default argument
# 3. Keyword argument 
# 4. Variable length Keyword arguments - **kwargs
# 5. Variable length Positional arguments - *args

def customer_details(cust_name, cust_age, cust_ID):
    print("Customer Name: ", cust_name)
    print("Customer Age: ", cust_age)
    print("Customer ID: ", cust_ID)

name = input("Enter name: ")
age = int(input("Enter age: "))
employee_ID = input("Enter ID: ")

customer_details(name, age, employee_ID)