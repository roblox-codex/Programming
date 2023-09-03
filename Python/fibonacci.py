# Generate Fibonacci sequence
n = int(input("Enter the number of Fibonacci terms to generate: "))

# Initialize the first two terms
a, b = 0, 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    count = 0
    while count < n:
        print(a)
        next_term = a + b
        a = b
        b = next_term
        count += 1
