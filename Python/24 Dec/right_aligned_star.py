def print_right_aligned_pyramid(height):
    for i in range(1, height + 1):
        stars = "*" * i
        print(stars.rjust(height))

try:
    height = int(input("Enter the height: "))
    print_right_aligned_pyramid(height)
except ValueError:
    print("Please enter a valid integer for the height.")
