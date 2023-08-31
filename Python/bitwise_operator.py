x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

# Bitwise AND
result_and = x & y
print("Bitwise AND:", result_and, "Binary:", bin(result_and)) # bin(result_and) it prints the binary of the result

# Bitwise OR
result_or = x | y
print("Bitwise OR:", result_or, "Binary:", bin(result_or)) # bin(result_or) it prints the binary of the result

# Bitwise XOR
result_xor = x ^ y
print("Bitwise XOR:", result_xor, "Binary:", bin(result_xor)) # bin(result_xor) it prints the binary of the result

# Bitwise NOT
x = int(input("Enter value of x: "))
result_not = ~x
print("Bitwise NOT:", result_not, "Binary:", bin(result_not)) # bin(result_not) it prints the binary of the result

# Left Shift
x = int(input("Enter value of x: "))
shift_amount = int(input("Enter value of shift: "))  # How much shift you want
result_left_shift = x << shift_amount
print("Left Shift:", result_left_shift, "Binary:", bin(result_left_shift)) # bin(result_left_shift) it prints the binary of the result

# Right Shift
x = int(input("Enter value of x: "))
shift_amount = int(input("Enter value of shift: "))  # How much shift you want
result_right_shift = x >> shift_amount
print("Right Shift:", result_right_shift, "Binary:", bin(result_right_shift)) # bin(result_right_shift) it prints the binary of the result
