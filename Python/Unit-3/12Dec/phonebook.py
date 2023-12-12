import pickle

def load_phonebook(filename):
    try:
        with open(filename, 'rb') as file:
            phonebook = pickle.load(file)
        return phonebook
    except FileNotFoundError:
        return {}

def save_contact(name, phone_number, filename):
    # Load existing contacts
    phonebook = load_phonebook(filename)

    # Add or update the new contact
    phonebook[name] = phone_number

    # Save the updated contacts back to the file
    with open(filename, 'wb') as file:
        pickle.dump(phonebook, file)

def main():
    filename = 'phonebook.bin'

    while True:
        name = input("Enter contact name ('exit' to stop): ")
        
        # Exit loop if the user enters 'exit'
        if name.lower() == 'exit':
            break

        phone_number = input("Enter phone number: ")
        save_contact(name, phone_number, filename)
        print("Contact saved.")

if __name__ == "__main__":
    main()
