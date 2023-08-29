# Python program to convert into decimal

a1 = input("Enter value in binary: ")
b1 = input("Enter value in octal: ")
c1 = input("Enter value in hexadecimal: ")

a = int(a1, 2) 
print("Decimal of binary:", a)

b = int(b1, 8) 
print("Decimal of octal:", b)

c = int(c1, 16) 
print("Decimal of hexadecimal:", c)


