def is_geometric_progression(seq):
    if len(seq) < 2:
        return True  

    common_ratio = seq[1] / seq[0]

    for i in range(2, len(seq)):
        if seq[i] / seq[i-1] != common_ratio:
            return False

    return True

try:
    sequence = input("Enter numbers separated by spaces: ")
    sequence = list(map(float, sequence.split()))
except ValueError:
    print("Invalid input.")
    exit()

if is_geometric_progression(sequence):
    print("The given sequence is a Geometric Progression (GP).")
else:
    print("The given sequence is not a Geometric Progression (GP).")
