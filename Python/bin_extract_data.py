import struct

def read_binary_file(file_path):
    # Open the file in binary mode
    with open(file_path, "rb") as file:
        # Get the file size
        file_size = file.seek(0, 2)

        # Go back to the beginning of the file
        file.seek(0)

        # Read the binary data from the file
        data = file.read(file_size)

    return data

def extract_data(binary_data):
    # Unpack the binary data
    unpacked_data = struct.unpack(">IIIIII", binary_data)

    return unpacked_data

def main():
    file_path = "binary_file.bin"
    binary_data = read_binary_file(file_path)
    data = extract_data(binary_data)
    print("Extracted data: ", data)

if __name__ == "__main__":
    main()
