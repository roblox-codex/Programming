# Using a while loop to calculate the factorial of a number

num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial:", factorial)
