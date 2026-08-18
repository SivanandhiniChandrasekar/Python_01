# Dictionary
# {}
# Key - Value
# {
#  "Name": "Sanjay",
#  "DOB": "12-04-2000",
#  "Schooling": "",
#  ""   
# }
# Name, DOB, Schooling - Keys

# CRUD - Create, Read, Update, Delete

# Creating a dictionary
d = {}
d = dict()
print(type(d))
student = {
    "Name": "Ashwini",
    "DOB": "14-08-2000",
    "Marks": [90, 87, 76, 98, 59]
}

# # Reading Keys only
print(student.keys())
for i in student.keys():
    print(i)

# # # Reading Values only
print(student.values())

# Reading Both
print(student.items())
for i, j in student.items():
    print(i, ":",j)


print(student['Subject'])

print(student.get("Subject", 5))

# Insertion
student['Subject'] = 5
print(student)

# Update
student["Name"] = "Sathya"

print(student)
student.update(
    {'Name': "Prabha",
     "Age": 21}
)

print(student)

# Deletion
del student['Age']
print(student)

# del student 
print(student)

temp = student.pop('Age', 0)
print(temp)
print(student)

