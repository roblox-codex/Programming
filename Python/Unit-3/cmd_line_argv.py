import sys

# Check if at least two command-line arguments are provided
if len(sys.argv) < 3:
    print("Usage: python script.py <num1> <num2> ... <numN>")
    sys.exit(1)

# Extract numbers from command-line arguments (starting from index 1)
numbers = [float(arg) for arg in sys.argv[1:]]

# Calculate the sum of the numbers
sum_of_numbers = sum(numbers)

# Print the sum
print("Sum of Numbers:", sum_of_numbers)
