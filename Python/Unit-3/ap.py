def is_arithmetic_progression(seq):
    if len(seq) < 2:
        return True  

    common_difference = seq[1] - seq[0]

    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != common_difference:
            return False

    return True

try:
    sequence = input("Enter a sequence of numbers separated by spaces: ")
    sequence = list(map(int, sequence.split()))
except ValueError:
    print("Invalid input. Please enter valid numbers separated by spaces.")
    exit()

if is_arithmetic_progression(sequence):
    print("The given sequence is an Arithmetic Progression (AP).")
else:
    print("The given sequence is not an Arithmetic Progression (AP).")
