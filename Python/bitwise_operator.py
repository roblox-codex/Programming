x = int(input("Enter value of x:- "))
y = int(input("Enter value of y:- "))

# Bitwise AND
result_and = x & y
print("Bitwise AND:", result_and)  

# Bitwise OR
result_or = x | y
print("Bitwise OR:", result_or)    

# Bitwise XOR
result_xor = x ^ y
print("Bitwise XOR:", result_xor)  

# Bitwise NOT
x = int(input("Enter value of x:- "))
result_not = ~x
print("Bitwise NOT:", result_not) 

# Left Shift
x = int(input("Enter value of x:- "))
shift_amount = int(input("Enter value of shift:- ")) # How much shift you want
result_left_shift = x << shift_amount
print("Left Shift:", result_left_shift)  

# Right Shift
x = int(input("Enter value of x:- ")) 
shift_amount = int(input("Enter value of shift:- ")) # How much shift you want
result_right_shift = x >> shift_amount
print("Right Shift:", result_right_shift)  
