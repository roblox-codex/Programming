# Program to create byte type array 

elements = [10, 20, 30, 40, 0, 50]

# Convert the list into bytes type array
x = bytes(elements)

# Retrieve elements from x using for loop
for i in x: print(i)

###############################################################################
# User input based

# Take input from the user for creating the byte array
elements = []
n = int(input("Enter the number of elements: "))
for _ in range(n):
    value = int(input("Enter an element: "))
    elements.append(value)

# Convert the list into bytes type array
x = bytes(elements)

# Retrieve elements from x using a for loop
for i in x:
    print(i)
