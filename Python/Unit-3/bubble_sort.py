def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Take input from the user
try:
    input_numbers = input("Enter numbers separated by space: ")
    unsorted_list = [int(num) for num in input_numbers.split()]
except ValueError:
    print("Invalid input. Please enter numbers separated by space.")
    exit()

# Call bubble_sort function to sort the list
bubble_sort(unsorted_list)

# Display the sorted array
print("Sorted array:", unsorted_list)
