def find_largest_and_smallest(sequence):
    if not sequence:
        return None, None 

    largest = smallest = sequence[0]

    for num in sequence:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest

def main():
    try:
        input_sequence = input("Enter a sequence of numbers separated by spaces: ")
        sequence = tuple(map(float, input_sequence.split())) 

        largest, smallest = find_largest_and_smallest(sequence)

        if largest is not None and smallest is not None:
            print("Largest number:", largest)
            print("Smallest number:", smallest)
        else:
            print("The sequence is empty.")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by spaces.")

if __name__ == "__main__":
    main()
