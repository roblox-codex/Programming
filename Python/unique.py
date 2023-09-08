def find_unique_numbers(input_list):
    unique_numbers = set(input_list)
    return list(unique_numbers)

numbers = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

# Find unique numbers
unique_numbers = find_unique_numbers(numbers)

# Display the unique numbers
print("Unique numbers:", unique_numbers)
