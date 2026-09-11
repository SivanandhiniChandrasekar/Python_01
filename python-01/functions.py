# functions - a block of code that performs a specific task which improves code reusability...

# Why function - Code reusability, reduce code duplication, easy to understand

# finTech_xyz-module
# Function Creation
# def greet(name):
#     print("Hello "+ name +" !..")
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

# def customer_details(cust_name , cust_age , cust_ID):
#     print("Customer Name:", cust_name)
#     print("Customer Age:", cust_age)
#     print("Customer ID:", cust_ID)

# name = input("Enter name: ")
# age = int(input("Enter age: "))
# employee_ID = input("Enter ID: ")

# customer_details(cust_age= age, cust_name = name, cust_ID=employee_ID)

# Variable length Keyword Argument
# def bank_details(bank_name,**bank):
#     print(bank, bank_name)
#     for i in bank:
#         print(i, bank[i])

# bank_details("Canara",name = "Nandhini", account_num = 223123123, transactions = 200, balance_amount = 2000, account_status = "Active")

# Variable length positional argument
def bank(*bank,custname):
    print(bank)
    print(custname)
bank(0, 123435, "Available balance: 9092", custname="Nandhini")