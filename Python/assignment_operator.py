# Get user input for variables a and b
a = float(input("Enter the value for 'a': "))
b = float(input("Enter the value for 'b': "))

# Assignment operator (=)
c = a + b
print("c =", c)  

# Addition assignment operator (+=)
a += b
print("a =", a)  

# Subtraction assignment operator (-=)
a -= b
print("a =", a) 

# Multiplication assignment operator (*=)
a *= b
print("a =", a)  

# Division assignment operator (/=)
a /= b
print("a =", a) 

# Floor Division assignment operator (//=)
a //= b
print("a =", a)  

# Modulus assignment operator (%=)
a %= b
print("a =", a)  

# Exponentiation assignment operator (**=)
a **= b
print("a =", a) 

# Bitwise AND assignment operator (&=)
a = int(a)
a &= int(b)
print("a =", a) 

# Bitwise OR assignment operator (|=)
a = int(a)
a |= int(b)
print("a =", a) 

# Bitwise XOR assignment operator (^=)
a = int(a)
a ^= int(b)
print("a =", a) 

# Bitwise Left Shift assignment operator (<<=)
a = int(a)
a <<= 2
print("a =", a) 

# Bitwise Right Shift assignment operator (>>=)
a = int(a)
a >>= 2
print("a =", a) 
