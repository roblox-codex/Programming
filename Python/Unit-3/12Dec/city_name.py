def store_city_in_file(file_path, city_name):
	with open(file_path, 'a') as file:
			file.write(city_name + '\n')
	print(f"City '{city_name}' stored successfully.")

def search_city_in_file(file_path, city_name):
	with open(file_path, 'r') as file:
			record_number = 0
			city_found = False
			while True:
					position = file.tell()
					line = file.readline()
					if not line:
							break
					record_number += 1
					if city_name in line:
							print(f"City '{city_name}' found in record number {record_number}")
							city_found = True
							break
					file.seek(position + len(line))

			if not city_found:
					print(f"City '{city_name}' not found in the file.")

file_path = 'city_name.txt'

while True:
	print("\nOptions:")
	print("1. Store City")
	print("2. Search City")
	print("3. Exit")

	choice = input("Enter your choice (1/2/3): ")

	if choice == '1':
			city_to_store = input("Enter the city name to store: ")
			store_city_in_file(file_path, city_to_store)
	elif choice == '2':
			city_to_search = input("Enter the city name to search: ")
			search_city_in_file(file_path, city_to_search)
	elif choice == '3':
			print("Exiting the program.")
			break
	else:
			print("Invalid choice. Please enter 1, 2, or 3.")
