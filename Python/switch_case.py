def case_one():
    print("You selected Case 1")

def case_two():
    print("You selected Case 2")

def case_three():
    print("You selected Case 3")

def default_case():
    print("Invalid choice")

# Mapping case values to corresponding functions
switch_dict = {
    1: case_one,
    2: case_two,
    3: case_three
}

choice = int(input("Enter a choice (1-3): "))

# Get the corresponding function from the dictionary and execute it
selected_case = switch_dict.get(choice, default_case)
selected_case()
