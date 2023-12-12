import pickle
import mmap

def load_phonebook(filename):
    try:
        with open(filename, 'rb') as file:
            phonebook = pickle.load(file)
        return phonebook
    except FileNotFoundError:
        return {}

def show_all_contacts(phonebook):
    print("\nAll Contacts:")
    for name, phone_number in phonebook.items():
        print(f"{name}: {phone_number}")

def modify_contact(phonebook, name):
    if name in phonebook:
        new_phone_number = input(f"Enter new phone number for {name}: ")
        phonebook[name] = new_phone_number
        print(f"Contact details for {name} modified.")
    else:
        print(f"Contact with name {name} not found.")

def save_phonebook(phonebook, filename):
    with open(filename, 'wb') as file:
        mmapped_file = mmap.mmap(file.fileno(), 0)
        mmapped_file.write(pickle.dumps(phonebook))

def main():
    filename = 'phonebook.bin'

    # Load existing phonebook
    phonebook = load_phonebook(filename)

    while True:
        print("\na) Show all Contacts")
        print("b) Modify Contact details")
        print("c) Exit")

        choice = input("Enter your choice (a/b/c): ")

        if choice == 'a':
            # Reload phonebook for display
            phonebook = load_phonebook(filename)
            show_all_contacts(phonebook)
        elif choice == 'b':
            name = input("Enter the name: ")
            modify_contact(phonebook, name)
        elif choice == 'c':
            save_phonebook(phonebook, filename)
            print("Phonebook saved.")
            break
        else:
            print("Invalid choice. Please enter a, b, or c.")

if __name__ == "__main__":
    main()
