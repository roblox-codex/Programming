def print_left_aligned_pyramid(height):
    for i in range(1, height + 1):
        stars = "*" * i
        print(stars.ljust(height))

try:
    height = int(input("Enter the height: "))
    print_left_aligned_pyramid(height)
except ValueError:
    print("Please enter a valid integer for the height.")
